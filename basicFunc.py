#Another global module. This one is for modules.
import time
import asyncio
import platform
import sys
from datetime import datetime
import json
try:
    with open('config.json') as json_file:
        settings = json.load(json_file)
except Exception as e:
    TheError = {
        "status" : "Error",
        "error" : e
    }
    settings = TheError

#THE loading bar
def LoadingBar(value, endvalue, bar_length=20):
    """Loading bar cool right!"""

    percent = float(value) / endvalue #makes it percentage certified
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\r[{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

class colour:
    #All this mess is because they dont show well at all on some systems. This is a basic estimate of what system this will work on
    PermittedOS = ["Linux", "Darwin"]
    CurrentOS = platform.system()
    try:
        settings["ExperimantalMode"] = settings["ExperimantalMode"]
    except Exception:
        settings["ExperimantalMode"] = 0
    if CurrentOS in PermittedOS or settings["ExperimantalMode"] == 1:
        PURPLE = "\033[95m"
        CYAN = "\033[96m"
        DARKCYAN = "\033[36m"
        BLUE = "\033[94m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        NORMAL = "\033[0m"
    else:
        PURPLE = ""
        CYAN = ""
        DARKCYAN = ""
        BLUE = ""
        GREEN = ""
        YELLOW = ""
        RED = ""
        BOLD = ""
        UNDERLINE = ""
        NORMAL = ""



async def DateFormat(messageFormat, message):
    """Adds date etc to the line. Currently reserved for later"""
    return

def ConfigIntegrityCheck(config):
    """Checks the integrity of the config and whether or not it will crash Pycord"""
    if type(config) is dict:
        try:
            #only real way of trying i know
            coolVariable = config["lang"]
            coolVariable = config["token"]
            coolVariable = config["ExperimantalMode"]
            coolVariable = config["Messenger"]
            if type(coolVariable) is dict:
                int(coolVariable["channelId"])
                coolVariable["defaultGame"] = coolVariable["defaultGame"]
                coolVariable = config["Viewer"]
                if type(coolVariable) is dict:
                    Viewer = config["Viewer"]
                    int(Viewer["ViewAll"])
                    for x in Viewer["ChannelWhitelist"]:
                        int(x)
                    int(Viewer["TimeFormat"])
                    return True
                else:
                    return False
            return False
        except Exception:
            return False

def nn():
    """Creates an empry line"""
    print("\n")

def TimeFormat(FormatNr, Message):
    """Responsible for putting a time in front of the msg"""
    if TimeFormat == 0:
        return Message

    elif FormatNr == 1:
        Time = datetime.now().strftime('%H:%M:%S')
        return "[{}] {}".format(Time, Message)

    elif FormatNr == 2:
        Time = datetime.now().strftime('%H:%M')
        return "[{}] {}".format(Time, Message)
    
    elif FormatNr == 3:
        Time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return "[{}] {}".format(Time, Message)

    else:
        return Message

def JsonOpen():
    """Opens the json settings file and converts to dict"""
    try:
        with open('config.json') as json_file:
            data = json.load(json_file)
    except Exception as e:
        TheError = {
            "status" : "Error",
            "error" : e
        }
        data = TheError
    return data

class LText:
    """The multilang class."""
    if settings["lang"].lower() == "gb":
        #English Commands
        CommandIntro = "The list of available commands is"
        HelpExplain = "Shows this message"
        FileExplain = "Sends a file located at a given path"
        GameExplain = "Sets a custom playing presence (use off for none)"
        ExitExplain = "Logs out and quits Pycord"

        StartupLoading = "Loading Pycord Messenger..."
        StartupLoadingViewer = "Loading Pycord Viewer..."
        BetaNotice = "This is still a work in progress so it shall not represent the final product."
        
        LoadingDone = " Loading finished!\nLogged into Discord via"
        GameChangingError = "Game Changing: {}"
        ModuleError = "\nCritical error occured during imports of critical modules!"
        ConfigInvalid = "Failed verifying config file! Make sure it exists and it matches the newest version available on GitHub"
        EmptyMessageError = "Unable to send empty messages!"
        FileSendingError = "File sending: {}"
        MessageSendingError = "Mesage sending: {}"
        LoginError = "Login : {}"

        ErrorMessage = "An error has occured with Pycord!\nError: {}"

        #Cotribution Table
        ContributionThanks = "Thanks to all these people who contributed to the project"
        RealistikContrib = "Coding, Polish Translation"
        DragoContrib = "French translation"
        CedContrib = "German translation"

    if settings["lang"].lower() == "fr":
        CommandIntro = "La liste de commandes disponibles sont"
        HelpExplain = "Montre ce message"
        FileExplain = "Envoi un fichier situé à un chemin spécifique"
        GameExplain = "Définit un message de jeu personnalisé (utilise 'off' pour aucun)"
        ExitExplain = "Déconnecte et quitte Pycord"

        StartupLoading = "Chargement de Pycord Messagerie..."
        StartupLoadingViewer = "Chargement de Pycord Visionneuse..."
        BetaNotice = "Ceci est encore un travaux en cours donc ce ne devrait pas représenter le produit final."
        
        LoadingDone = " Chargement terminé!\nConnecté sur Discord avec"
        GameChangingError = "Changement de jeu: {}"
        ModuleError = "\nErreur criticale rencontrée durant l'importation de modules criticals! !"
        ConfigInvalid = "Échec de la verification du fichier de configuration! Assurez-vous que le fichier existe et qu'il correspond à la plus nouvelle version disponible sur GitHub"
        EmptyMessageError = "Impossible d'envoyer des messages vide!"
        FileSendingError = "Envoi du fichier: {}"
        MessageSendingError = "Envoi du message: {}"
        LoginError = "Connection : {}"

        ErrorMessage = "Une erreur est survenue avec Pycord!\nErreur: {}"

        #Cotribution Table
        ContributionThanks = "Merci à tous ces personnes qui ont contribué à ce projet"
        RealistikContrib = "Codage, Traduction Polonaise"
        DragoContrib = "Traduction Française"
        CedContrib = "Traduction Allemande"

    if settings["lang"].lower() == "de":
        CommandIntro = "Die Liste der verfügbaren Befehle ist"
        HelpExplain = "Zeigt diese Nachricht"
        FileExplain = "Sendet eine Datei, die sich an einem bestimmten Pfad befindet"
        GameExplain = "Setzt einen benutzerdefinierten Spiele Status (Benutze off für keinen)"
        ExitExplain = "Abmelden und das verlassen von Pycord"

        StartupLoading = "Laden des Pycord Messenger..."
        StartupLoadingViewer = "Laden des Pycord Viewer..."
        BetaNotice = "Dies ist noch in Arbeit, so dass es nicht das Endprodukt darstellen soll."
        
        LoadingDone = "Laden abgeschlossen!\nEingeloggt in Discord über"
        GameChangingError = "Spieländerung: {}"
        ModuleError = "\nEin kritischer Fehler ist beim Importieren von kritischen modulen aufgetreten!"
        ConfigInvalid = "Überprüfung der Konfigurationsdatei fehlgeschlagen! Stellen sie sicher, das sie existiet und es entspricht der neusten Version auf GitHub"
        EmptyMessageError = "leere Nachrichten können nicht gesendet werden!"
        FileSendingError = "Datei senden: {}"
        MessageSendingError = "Nachricht senden: {}"
        LoginError = "Anmelden : {}"

        ErrorMessage = "Ein Fehler ist mit Pycord aufgetreten!\nFehler: {}"

        #Cotribution Table
        ContributionThanks = "Danke an all die Leute die beim Projekt mit beigetragen haben"
        RealistikContrib = "Programmierung, Polnische Übersetzung"
        DragoContrib = "Französische Übersetzung"
        CedContrib = "Deutsche Übersetzung"

    if settings["lang"].lower() == "pl":
        #Polish commands
        CommandIntro = "Lista dostępnych komend jest"
        HelpExplain = "Pokazuje tą wiadomość"
        FileExplain = "Wysyła plik zlokalizowany w danej ścieżce"
        GameExplain = "Ustawia wiadomość 'grania' na podaną przez użytkownika (ustaw na off aby wyłączyć)"
        ExitExplain = "Wylogowuje się z Pycord"

        StartupLoading = "Ładowanie Pycord Messenger..."
        BetaNotice = "Jest to wciąż praca w toku, więc nie będzie reprezentować produktu końcowego."
        
        LoadingDone = " Ładowanie zakończone!\nZalogowany do Discord przez"
        GameChangingError = "Zmiana gry: {}"
        ModuleError = "\nWystąpił błąd krytyczny podczas importu krytycznych modułów!"
        ConfigInvalid = "Nie udało się zweryfikować pliku konfiguracyjnego! Upewnij się, że istnieje i odpowiada najnowszej wersji dostępnej na GitHub!"
        EmptyMessageError = "Nie można wysłać pustych wiadomości!"
        FileSendingError = "Wysyłanie pliku: {}"
        MessageSendingError = "Wysyłanie wiadomiści: {}"
        LoginError = "Logowanie się : {}"

        ErrorMessage = "Wystąpił błąd w Pycord!\nBłąd: {}"

        #Cotribution Table
        ContributionThanks = "Dziękuję wszystkim osobom, które odegrały rolę w tym projekcie"
        RealistikContrib = "Programowanie, Polskie tłumaczenie"
        DragoContrib = "Francuskie tłumaczenie"
        CedContrib = "Niemieckie tłumaczenie"

def ErrorMessage(message):
    """Template for error messages (not finished)"""
    print(LText.ErrorMessage.format(message))

async def AsyncErrorMessage(message):
    """Template for error messages. But guess what? It's asyncronous (not finished)"""
    print(LText.ErrorMessage.format(message))

def Contributors():
    """Displays contributors"""
    print("----------------------------------------------------------")
    print("{}".format(LText.ContributionThanks))
    print("RealistikDash        {}".format(LText.RealistikContrib))
    print("Dragoofficial        {}".format(LText.DragoContrib))
    print("TheRealCed           {}".format(LText.CedContrib))
    print("----------------------------------------------------------")
