# PyCord
This branch is almost ready. Just needs tweaks/is unfinished. This code has a chance of working but who knows...

Pycord is a simple Discord client created to bypass the restrictions on Discord by network owners.

# Tested Python Versions

Here is a list of tested Python versions.

3.6.5 - works with no issues

3.6.1 - works with no issues

2.7.10 - aiohttp requires 3.4.2 or higher

# Initial setup:

Setup:

-Create a bot on the Discord Developer Portal

-Get a token

-Run setup.py

-Edit both py files with your token.

![alt text](http://realistikdash.com/img/pycordToken.PNG)

# Troubleshooting
If the new responder gives you an error about local variables, enter '/changeid {your channel id}'

If you having an issue connecting, this could mean a few things. Firstly, it can mean you misentered the token. It can also mean you are entering an account from a new location and you need to verify the location via email. Lastly, it can mean the Discord API is blocked too. This can be solved by using a site like repl.it or a VPS to run Pycord.

# Pycord Resonder Commands

The responder has it's own commands to save you time coding them in. 

The currently available commands are:

| Command | Description |
| --- | --- |
| /help | Lists all the available commands. |
| /setgame | Sets your presence to a given input. |
| /sendfile | Sends a file with a given name. |
| /customsend | Lets you choose the variables such as the channel id, message and any other attributes. |
| /changeuser | Changes your Pycord username. |
| /sendtxt | Sends the contents of a specified txt file. (2000 characters max) |
| /changeid | Changes the channel id to which your messages are being sent to. |
| /shrug | Sends a ¯\_(ツ)_/¯ |
| /ping | Checks your connection to discord in ms (lower is better) |
| /exit | Logs off and exits Pycord |

# Pycord Viewer Focus Mode

Focus mode docuses on one channel and ignores the others. To enable it, set focusmode variable to 1 (keep it an int) and input a channel id (as a str). It all has a dedicated, commented section in the code so they are easy to find.

Here is an example (every channel has a different ID):

![alt text](http://realistikdash.com/img/focusExample.PNG)
