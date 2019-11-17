# Pycord
The simple kinda-discord client
![alt text](https://i.ussr.online/5db8da39579279.59374087-Pycord.png)

# What is this?
This is a rewrite of Pycord on the new Discord.py rewrite. It's aim is not only to move onto a new version of Discord.py but  to also move on from the caviates that plagued the previous versions of Pycord such as the try spam, lots of untested code and my rather limited knowledge of Python at the beginning of the project

# Downloads

Pycord Windows executables are currently available to download [here!](https://github.com/RealistikDash/Pycord/releases)

To get it to successfully launch, you'll need to download the latest config.json, edit it and done! No Python required.

# Contributors

| Person  | Contribution |
| ------------- | ------------- |
| RealistikDash  | Programmig, Polish traslation  |
| Dragoofficial | French translation  |
| TheRealCed | German translation  |

# Use examples of Pycord

This project began when my school blocked Discord. Because of this, I made a Discord message sender and viewer that can be easily ran on something like a VPS or repl.it (which is why it is console based).

With Pycord, you are able to send and recieve messages through a bot (user accounts might be a possibility **soon**) (Update: found a decent way of getting it to work so probably will come soon)

# Compatibility

| System  | Python | Discord.py | Status |
| ------------- | ------------- | ------------- | ------------- |
| Windows 10  | 3.7.4  | 1.2.3  | Works!  |
| Repl.it (Linux) | 3.7.4  | 1.2.4  | Inactivity Crashes |
| Ubuntu | 3.6.8  | 1.2.3  | Inactivity Crashes |

# Configuration

This section's aim is to explain each variable of the config.json file.

```json
{
    "token" : "sampletoken",
    "ExperimantalMode" : 0,
    "Messenger" : {
        "channelId" : 458748688504848396,
        "defaultGame" : "Example Game"
    },
    "Viewer" : {
        "ViewAll" : 0,
        "ChannelWhitelist" : [123456789, 123456789],
        "TimeFormat" : 1
    }
}
```

### Here is what each variable does.

`Token` - This is where the BOT token goes. This will be used to log into the Discord bot.

`ExperimentalMode` - If set to 1, it will enable some features that are either half working or may not work with some systems.

`Messenger` - A dictionary that stores all the Pycord Messenger configuration.

`Messenger>channelId` - The default channel id that the messages will be sent to

`Messenger>defaultGame` - This will be the default playing message upon opening Pycord Messenger. Set to "False" for none.

`Viewer` - A dictionary that stores all the Pycord Viewer configuration.

`Viewer>ViewAll` - If set to 1, all messages from all channels will be displayed in Pycord Viewer. If set to 0, only chanels in the next variable will be displayed.

`Viewer>ChannelWhitelist` - If ViewAll is set to 0, only channnels with their channel ids in this array will be displayed.

`Viewer>TimeFormat` - Value of 0-3. Chooses which time format to use in front of messages displayed. 0 = None. 1 = H:M:S. 2 = H:M. 3 = D/M/Y H:M:S
