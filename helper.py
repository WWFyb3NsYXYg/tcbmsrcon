
rm_smb = ['§1', '§2', '§3', '§4', '§5', '§6', '§7', '§8',
          '§9', '§e', '§l', '§L', '§f', '§c', '§r', '-------']
temp_nick = ""
temp_donate = ""


def definition_butt():
    if (temp_donate == "Админ 👑"):
        return "admin"

    elif (temp_donate == "Модер 🆘"):
        return "moder"

    elif (temp_donate == "Помощник 🆘"):
        return "helper"

    elif (temp_donate == "Модератор 🆘"):
        return "moderator"

    elif (temp_donate == "Ютубер 🎥"):
        return "yt"

    elif (temp_donate == "Игрок 🤠"):
        return "default"

    else:
        return "err"
