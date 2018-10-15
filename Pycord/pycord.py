#The Pycord module.

#imports
from colorama import Fore, Back, Style
from colorama import init
#################

init()


#Loggers
def log(say): #Simple logger for quick modifications
    """Logs something with the Pycord info tag"""
    print(Fore.YELLOW + '[Pycord Log]', say)
    print(Fore.RESET)

def errorLog(error): #Simple error logger for quick modifications
    """Throws an error of choice with the Pycord tag"""
    print(Fore.RED + '[Pycord Error]', error)
    print(Fore.RESET)
