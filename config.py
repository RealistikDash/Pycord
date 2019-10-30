#This is the Pycord Rewrite config file. This is used by both Messenger and Viewer
settings = {
    "token" : "BotToken",
    "ExperimantalMode" : 1, #enables features that might not be working well
    "Messenger" : {
        "channelId" : 458748688504848396, #Make sure its an int
        "defaultGame" : "Example Game" #set to bool of False to not have one
    },
    "Viewer" : {
        "ViewAll" : 0, #If set to 1, it will show messages in all channels (NOT RECOMMENDED)
        "ChannelWhitelist" : [456091543669833728, 453226417782784000], #List of channel ids (ints) to show msgs from if ViewAll == 0
        "TimeFormat" : 1 #Chooses between time formats 0-3
    }
}

script = { #I might include a script system similar to Discord Message Bot
    "ScriptName" : "Sample",
    "ScriptCreator" : "Sample"
}
