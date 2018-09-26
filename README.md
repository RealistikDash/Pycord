# PyCord
Pycord is a simple Discord client created to bypass the restrictions on Discord by network owners.

# Initial setup:

Setup:

-Create a bot on the Discord Developer Portal

-Get a token

-Open cmd in the Pycord folder

-Run 'pip install -r requirements.txt'

-Edit both py files with your token.

# Troubleshooting
If the new responder gives you an error about local variables, enter '/changeid {your channel id}'

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
| /exit | Logs off and exits Pycord |

# Pycord Viewer Focus Mode

Focus mode docuses on one channel and ignores the others. To enable it, set focusmode variable to 1 (keep it an int) and input a channel id (as a str). It all has a dedicated, commented section in the code so they are easy to find.
