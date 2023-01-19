import config

if (config.language == 'ua'):
    start_message_ok = ('Вітаю, {}!\n'
                        'Я передам будь-які твої команди на сервер\n'
                        'Не соромся звертатися до мене в чатах. Я видалю свій '
                        '@username з команди')

    start_message_err = "В тебе немає доступу для використання цього бота."
    input_nick = "✍ Введіть нік користувача"
    cancel_ok = "Дія скасована"
    choose_donate = "Оберіть донат 🗒️"
    err_choose_donate = "Неправильне введення. Оберіть донат ІЗ СПИСКУ 🗒️"
    success = "Успіх ✅"
    input_amount = "Введіть суму поповнення 🤑"
    err_input_amount = "Неправильне введення. Введіть суму цифрами 🤑"
    input_nick_ban = "✍ Введіть нік користувача (через пробіл причину бана, не обов'язково)"
    ban_ok = "Гравця заблоковано ⛔️"
    pardon_ok = "Гравця розблоковано ✅"
    rst_warning = "⚠️ ВИ ВПЕВНЕНІ ЩО ХОЧЕТЕ ПЕРЕЗАВАНТАЖИТИ СЕРВЕР? ⚠️"
    rst_ok = "Сервер перезавантажився 🕐"

    get_donate_btn = "Видача донату 🍩"
    issuance_currency_btn = "Видача валюти гравцю 💵"
    ban_btn = "Заблокувати Гравця ⛔️"
    pardon_btn = "Розблокувати Гравця ✅"
    restart_btn = "Перезавантажити сервер 🔄"
    cancel_rst_btn = "Скасування 🟢"
    run_rst_btn = "Так, хочу перезавантажити 🔴"
    cancel_btn = "Cкасування ❌"

elif (config.language == 'en'):
    start_message_ok = ('Hello, {}!\n'
                        'I will pass any of your commands to the server\n'
                        'Feel free to contact me in chats. I will delete mine '
                        '@username from the command')

    start_message_err = "You do not have access to use this bot."
    input_nick = "✍ Enter username"
    cancel_ok = "Action canceled"
    choose_donate = "Choose a donation 🗒️"
    err_choose_donate = "Invalid input. Choose a donation FROM THE LIST 🗒️"
    success = "Success ✅"
    input_amount = "Enter the replenishment amount 🤑"
    err_input_amount = "Invalid input. Enter amount in numbers 🤑"
    input_nick_ban = "✍ Enter the user's nickname (separated by a space, the reason for the ban, optional)"
    ban_ok = "Player banned ⛔️"
    pardon_ok = "Player unbanned ✅"
    rst_warning = "⚠️ ARE YOU SURE YOU WANT TO RESTART THE SERVER? ⚠️"
    rst_ok = "Server rebooted 🕐"

    get_donate_btn = "Issuing a donation 🍩"
    issuance_currency_btn = "Issuance of currency to the player 💵"
    ban_btn = "Ban player ⛔️"
    pardon_btn = "Unban a player ✅"
    restart_btn = "Restart server 🔄"
    cancel_rst_btn = "Cancel 🟢"
    run_rst_btn = "Yes, I want to restart 🔴"
    cancel_btn = "Cancel ❌"

elif (config.language == 'ru'):
    start_message_ok = ('Привет, {}!\n'
                        'Я передам любые твои команды на сервер\n'
                        'Не стесняйся обращаться ко мне в чатах. Я удалю свой '
                        '@username из команды')

    start_message_err = "У тебя нет доступа для использования этого бота."
    input_nick = "✍ Введите ник пользователя"
    cancel_ok = "Действие отменено"
    choose_donate = "Выберите донат 🗒️"
    err_choose_donate = "Неправильный ввод. Выберите донат ИЗ СПИСКА 🗒️"
    success = "Успех ✅"
    input_amount = "Введите сумму пополнения 🤑"
    err_input_amount = "Неправильный ввод. Введите сумму цифрами 🤑"
    input_nick_ban = "✍ Введите ник пользователя (через пробел причину бана, не обязательно)"
    ban_ok = "Игрок забанен ⛔️"
    pardon_ok = "Игрок разбанен ✅"
    rst_warning = "⚠️ ВЫ УВЕРЕНЫ ЧТО ХОТИТЕ ПЕРЕЗАГРУЗИТЬ СЕРВЕР? ⚠️"
    rst_ok = "Сервер перезагрузился 🕐"

    get_donate_btn = "Выдача доната 🍩"
    issuance_currency_btn = "Выдача валюты игроку 💵"
    ban_btn = "Забанить игрока ⛔️"
    pardon_btn = "Разбанить игрока ✅"
    restart_btn = "Перезапустить сервер 🔄"
    cancel_rst_btn = "Отмена 🟢"
    run_rst_btn = "Да, хочу перезагрузить 🔴"
    cancel_btn = "Отмена ❌"
