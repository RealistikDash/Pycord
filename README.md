[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# PyCord

Pycord is a simple Discord client created to bypass the restrictions on Discord by network owners.

Branch layout

| Branch | Description |
| --- | --- |
| master | Most stable and most bug-free. Use it if you want a the most stable experiance. |
| almost-done | More buggy but has newer features and is updated more. The code is decent. Use it for the superior features. |

# Tested Python Versions

Here is a list of tested Python versions.

3.6.5 - works with no issues

3.6.1 - works with no issues

2.7.10 - aiohttp requires 3.4.2 or higher

# Pre installation notes!

-Make sure your Python is added to path! Folow [this](https://github.com/RealistikDash/Pycord/wiki/How-to-add-Python-to-path%3F-(Windows)) if you don't know how to.

# Initial setup:

Setup:

-Create a bot on the Discord Developer Portal

-Get a token

-Run setup.py. It will setup everything for you. All you will need to do is enter the channel id, bot token and if you want to use focus mode.

-Enjoy

# Editing settings.py

While you can edit it using a text editor, you can also use setup.py and it's new editor because why not?

# Troubleshooting
The responder has been equipped with error handling. However, if that still doesn't fix it, try these steps.

If the new responder gives you an error about local variables, enter '/changeid {your channel id}'

If you having an issue connecting, this could mean a few things. Firstly, it can mean you misentered the token. It can also mean you are entering an account from a new location and you need to verify the location via email. Lastly, it can mean the Discord API is blocked too. This can be solved by using a site like repl.it or a VPS to run Pycord. A VPN should also be fine.

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
| /embed | Sends an embed with given variables (Usage: /embed [title] - [content]) |
| /changeid | Changes the channel id to which your messages are being sent to. |
| /shrug | Sends a ¯\_(ツ)_/¯ |
| /ping | Checks your connection to discord in ms (lower is better) |
| /clear | Clears the screen |
| /exit | Logs off and exits Pycord |

# Pycord Viewer Focus Mode

Focus mode focuses on one channel and ignores the others. It is now controllable via the new setup.
