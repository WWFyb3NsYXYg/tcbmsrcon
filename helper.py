import donations
import locale
from aiogram import types


rm_smb = ['§1', '§2', '§3', '§4', '§5', '§6', '§7', '§8',
          '§9', '§e', '§l', '§L', '§f', '§c', '§r', '-------']

dn_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

temp_nick = ""

temp_donate = ""


def definition_butt():
    for i in range(len(donations.donation)):
        if (temp_donate == donations.donation[i][1]):
            return (donations.donation[i][0])
        elif (i+1 == len(donations.donation)):
            return ("err")


dn_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)


def kbd_gen():
    for i in range(len(donations.donation)):
        dn_kb.row(types.KeyboardButton(text=donations.donation[i][1]))
        if (i+1 == len(donations.donation)):
            dn_kb.add(types.KeyboardButton(text=locale.cancel_btn))


kb = [
    [
        types.KeyboardButton(text=locale.get_donate_btn),
        types.KeyboardButton(text=locale.issuance_currency_btn),

    ],
    [
        types.KeyboardButton(text=locale.pardon_btn),
        types.KeyboardButton(text=locale.ban_btn),
    ],
    [
        types.KeyboardButton(text=locale.restart_btn),
    ],
]

kb_ext = [
    [
        types.KeyboardButton(text=locale.cancel_btn),
    ],]

kb_rld = [
    [
        types.KeyboardButton(text=locale.cancel_rst_btn),
    ],
    [
        types.KeyboardButton(text=locale.run_rst_btn),
    ],
]

menu_kb = types.ReplyKeyboardMarkup(keyboard=kb)
ext_kb = types.ReplyKeyboardMarkup(keyboard=kb_ext)
rld_kb = types.ReplyKeyboardMarkup(keyboard=kb_rld)
