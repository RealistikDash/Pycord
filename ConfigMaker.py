from basicFunc import *
import json
import os
import getpass
try:
    import requests
    RequestsPresent = True
except Exception:
    RequestsPresent = False

sp = "----------------------------------"

SampleConfig = {
    "lang" : "",
    "token" : "",
    "ExperimantalMode" : 0,
    "Messenger" : {
        "channelId" : 0,
        "defaultGame" : "e"
    },
    "Viewer" : {
        "ViewAll" : 0,
        "ChannelWhitelist" : [],
        "TimeFormat" : 1
    }
}

while True:
    print("Welcome to the Pycord Setup!")
    print("Choose your action.")
    print(sp)
    print("1 - Create Config")
    print("2 - Download modules*")
    print("3 - Exit")
    Choice = input("> ")

    if Choice == "3":
        exit()
    
    if Choice == "2":
        print("WARNING!")
        print("This will only work with the unbuilt version (.py file format) and is unnecessary/will not work with the executables (.exe file format)")
        print("This also requires you to have Python in your path. To do that, follow the Pycord wiki on GitHub.")
        print("Are you sure you want to proceed (y/N)")
        Permit = input("[y/N] > ")
        if Permit.lower() == "y":
            if RequestsPresent == False:
                os.system("python -m pip install requests")
            ModuleURL = "https://raw.githubusercontent.com/RealistikDash/Pycord/rewite/requirements.txt"
            Modules = requests.get(ModuleURL, verify=True)
            Modules = Modules.text
            ModulesArray = Modules.split("\n")
            for thing in ModulesArray:
                if thing == "":
                    pass
                else:
                    try:
                        os.system("pip install {}".format(thing))
                    except Exception as e:
                        print("An error has occured! Error {}".format(e))
            print("Done!")
            nn()
        
        else:
            print("Ok. Cancelled.")
            nn()

    if Choice == "1":
        CurrentThing = JsonOpen()
        if CurrentThing["status"] == "fine":
            print("A config already exists! Proceeding will overwrite it! Are you sure you want to continue?")
            WarningAcceptance = input("[y/N] > ")
            if WarningAcceptance.lower() == "y":
                GoAhead = True
            else:
                GoAhead = False
        else:
            GoAhead = True

        if GoAhead == False:
            print("Ok. Cancelled.")
            nn()
        
        else:
            print(sp)
            print("Enter your language")
            print("1. English")
            print("2. French")
            print("3. German")
            print("4. Polish")
            lang = input("Lang > ")
            if lang == "2":
                SampleConfig["lang"] = "fr"
            if lang == "3":
                SampleConfig["lang"] = "de"
            if lang == "4":
                SampleConfig["lang"] = "pl"
            else:
                SampleConfig["lang"] = "gb"
            
            print(sp)
            print("Enter your bot token (invisible)")
            SampleConfig["token"] = getpass.getpass("Token > ")

            print(sp)
            print("What channel do you want messages to be sent and recieved from?")
            #Too lazy to do all the viewer things seperately
            Woring = False
            while Woring == False:
                ChId = input("Channel Id > ")
                try:
                    ChId = int(ChId)
                    Woring = True
                except Exception:
                    print("That doesn't look right...")
            SampleConfig["Messenger"]["channelId"] = ChId
            SampleConfig["Viewer"]["ViewAll"] = 0
            SampleConfig["Viewer"]["ChannelWhitelist"].append(ChId)

            print(sp)
            print("Do you want a custom Playing presence?")
            DAANSWER = input("[y/N] > ")
            if DAANSWER.lower() == "y":
                print("Enter the presence")
                while SampleConfig["Messenger"]["defaultGame"] != "e":
                    GameToPlay = input("Game > ")
                    if GameToPlay == "":
                        print("It can't be empty!")
                    else:
                        SampleConfig["Messenger"]["defaultGame"] = GameToPlay
            else:
                SampleConfig["Messenger"]["defaultGame"] = "False"

            print(sp)
            print("Lastly, what time format do you want to use?")
            print(TimeFormat(0, "0"))
            print(TimeFormat(1, "1"))
            print(TimeFormat(2, "2"))
            print(TimeFormat(3, "3"))
            ResponsesAvi = ["0", "1", "2", "3"]
            Time = "cool"
            while Time not in ResponsesAvi:
                Time = input("Time Format > ")
                if Time in ResponsesAvi:
                    SampleConfig["Viewer"]["TimeFormat"] = Time
                else:
                    print("That doesn't look right.")
            
            print(sp)
            print("Writing data...")

            with open("config.json", "w") as write_file:
                try:
                    json.dump(SampleConfig, write_file)
                except Exception as e:
                    print("An error has occured writing the data! Error {}".format(e))
            
            print("Done!")
            nn()
