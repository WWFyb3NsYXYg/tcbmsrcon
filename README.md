
# Telegram control bot for Minecraft server by RCON
  
## Установка

1. `pip install mcrcon` библиотека Python для управления сервером по протоколу RCON

2. Переменные (файл config.py)
   * `YOUR_TELEGRAM_BOT_TOKEN` - Токен вашего Telegram бота. Получить [@BotFather](https://telegram.me/BotFather)

   * `ADMINS_ID` - ID пользователей, имеющих доступ к использованию бота. Если несколько, перечислить через символ `_`. Получить ID можно в [@my_id_bot](https://telegram.me/my_id_bot)

   * `IP_MC_SERVER` - IP адресс вашего сервера

   * `PASS_RCON` – пароль для RCON подключения. Настраиваеться в файле сервера `server.properties`. [Посмотреть скриншот](https://user-images.githubusercontent.com/87089735/212674626-02da2339-2e61-4bfe-86f0-e0f6b2fd3540.png)


   * `PASS_PORT` (не обязательно, по умолчанию `25575`) – порт для RCON подключения
   
## Скриншот меню

<p align="center">
<img src="https://user-images.githubusercontent.com/87089735/212678716-549cd397-6662-4896-a8c8-6895b3d10496.jpg" height="600px">
<p>
  
  
## Функции

  * `Выдача доната` - посылает команду `lp user NICKNAME parent set DONATE`. 
    
    У DONATE есть значения: `admin`, `moder`, `helper`, `moderator`, `yt`, `default`

  * `Выдача валюты игроку` - посылает команду `eco give NICKNAME VALUE`. 

    VALUE в значение принимает только цифры
    
  * `Разбанить игрока` - посылает команду `pardon NICKNAME`. 
  
  * `Забанить игрока` - посылает команду `ban NICKNAME`. 

    При вводе ника игрока через пробел так же можно ввести причину бана.
   
  * `Перезапустить сервер` - посылает команду `reload`. В следующем пункте при выборе варианта `Да, хочу перезагрузить` будет отправлена команда `reload confirm`
  
  * Остальные команды просто писать в чат с ботом: `say hello`, `//help`. Можно использовать бота в группе. Обращяться тогда так: `/say hi@bot_username`, `//help@bot_username`
    

## Полезная информация
* [Заимствованный репозиторий](https://github.com/DavisDmitry/TeleMCRCON)
