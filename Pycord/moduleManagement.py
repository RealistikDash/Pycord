#The module managment tools for Pycord.
#Used for module installation and others.

#Required imports
import os
import pycord
#################


def installModule(module): #The module installer
  """Installs a module"""
  pycord.log("Installing {}...".format(module)) #Logs installing
  os.system("pip install {}".format(module)) #Installs the module
  
 
def installModuleVerbouse(module): #The module installer
  """Installs a module using pip with verbouse mode"""
  pycord.log("Installing {}...".format(module)) #Logs installing
  os.system("pip install -v {}".format(module)) #Installs the module (v flag for verbouse)
