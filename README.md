
# Telegram control bot for Minecraft server by RCON
  
## Installation

1. `pip install mcrcon` Python library for server management via RCON protocol

2. Variables (file config.py)
   * `YOUR_TELEGRAM_BOT_TOKEN` - Token of your Telegram bot. Receive [@BotFather](https://telegram.me/BotFather)

   * `ADMINS_ID` - ID of users who have access to use the bot. If there are several, list through a symbol `_`. You can get an ID at [@my_id_bot](https://telegram.me/my_id_bot)

   * `IP_MC_SERVER` - IP address of your server

   * `PASS_RCON` – password for RCON connection. Configurable in the server file `server.properties`. [View screenshot](https://user-images.githubusercontent.com/87089735/212674626-02da2339-2e61-4bfe-86f0-e0f6b2fd3540.png)


   * `PASS_PORT` (optional, default `25575`) – port for RCON connection
   *  You can also change the language of the bot. The `language` variable takes the values <img src="https://user-images.githubusercontent.com/87089735/213570989-5be18f9b-fb96-48ae-bb10-ed0b02ac971b.png" height="20px"> `ua`, <img src="https://user-images.githubusercontent.com/87089735/213571353-a9f45178-b7e0-41d0-8148-3241ec9d64b2.png" height="20px"> `en`, `ru`
   
## Menu screenshot


<p align="center">
<img src="https://user-images.githubusercontent.com/87089735/213577676-aaba8d0f-78ac-48d8-81b4-2637984c82f2.jpg" height="400px">
<img src="https://user-images.githubusercontent.com/87089735/213576186-c0690668-5733-4968-8062-b4ae79eb620d.jpg" height="400px">
<img src="https://user-images.githubusercontent.com/87089735/213577822-5d88ff3c-5c52-4af4-af11-f46d6aefd73d.jpg" height="400px">
<p>

  
## Functions

  * `Issuing a donation` - sends the command `lp user NICKNAME parent set DONATE`. 
    
    DONATE has meanings: `admin`, `moder`, `helper`, `moderator`, `yt`, `default`. 
    
    You can add your own privileges or change the configured ones in the file `donations.py`. 
  
    To add, separated by commas: ["donate tag for the command","Donation name that will be displayed in the keyboard"].  

  * `Issuance of currency to the player` - sends the command `eco give NICKNAME VALUE`.

    VALUE accepts only numbers
    
  * `Unban a player` - sends the command `pardon NICKNAME`.
  
  * `Ban player` - sends the `ban NICKNAME` command.

     When entering a player's nickname separated by a space, you can also enter the reason for the ban.
   
  * `Restart server` - sends a `reload` command. In the next paragraph, when choosing the option `Yes, I want to restart`, the command `reload confirm` will be sent
  
  * Other commands just write to the chat with the bot: `say hello`, `//help`. You can use the bot in a group. Then address like this: `/say hi@bot_username`, `//help@bot_username`
    

## Credits
  https://github.com/DavisDmitry/TeleMCRCON
