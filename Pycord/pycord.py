#The Pycord module.

#imports
from colorama import Fore, Back, Style
from colorama import init
#################

init()


#Loggers
def log(say): #Simple logger for quick modifications
    """Logs something with the Pycord info tag"""
    print(Fore.YELLOW + '[Pycord Log]', say, Fore.RESET)

def errorLog(error): #Simple error logger for quick modifications
    """Throws an error of choice with the Pycord tag"""
    print(Fore.RED + '[Pycord Error]', error, Fore.RESET)

def checkNumber(variable):
    """Checks if a given variable only consists of numbers"""
    try: #Attempts to turn the variable into and int
        variable = int(variable)
        return 'true'
    
    except Exception: #if it fails, false is returned
        return 'false'
