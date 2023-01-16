from aiogram import types

kb_dn = [
        [
            types.KeyboardButton(text="Админ 👑"),
            types.KeyboardButton(text="Модер 🆘"),
            types.KeyboardButton(text="Помощник 🆘"),
        ],
    [
            types.KeyboardButton(text="Модератор 🆘"),
            types.KeyboardButton(text="Ютубер 🎥"),
            ],
    [
            types.KeyboardButton(text="Игрок 🤠"),
            ],
    [
            types.KeyboardButton(text="Отмена ❌"),
            ],
]


kb = [
    [
        types.KeyboardButton(text="Выдача доната 🍩"),
        types.KeyboardButton(text="Выдача валюты игроку 💵"),

    ],
    [
        types.KeyboardButton(text="Разбанить игрока ✅"),
        types.KeyboardButton(text="Забанить игрока ⛔️"),
    ],
    [
        types.KeyboardButton(text="Перезапустить сервер 🔄"),
    ],
]

kb_ext = [
    [
        types.KeyboardButton(text="Отмена ❌"),
    ],]

kb_rld = [
    [
        types.KeyboardButton(text="Отмена 🟢"),
    ],
    [
        types.KeyboardButton(text="Да, хочу перезагрузить 🔴"),
    ],
]

menu_kb = types.ReplyKeyboardMarkup(keyboard=kb)
dn_kb = types.ReplyKeyboardMarkup(keyboard=kb_dn)
ext_kb = types.ReplyKeyboardMarkup(keyboard=kb_ext)
rld_kb = types.ReplyKeyboardMarkup(keyboard=kb_rld)
