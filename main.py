from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
import logging
import helper
import keyboards
from config import Configuration
from mcrcon import MCRcon

config = Configuration.from_env()

bot = Bot(config.token, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=config.log_level)
logger = logging.getLogger('bot')
logger.setLevel(config.log_level)


class set_donate(StatesGroup):
    wait_nick = State()
    wait_donate_n = State()
    wait_ban = State()
    wait_unban = State()
    wait_reload = State()
    wait_money = State()
    wait_nick_to_pay = State()

# -----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- START --------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(commands='start')
async def start(message: types.Message):
    if message.from_user.id in config.admins_list:
        text = ('Привет, {}!\n'
                'Я передам любые твои команды на сервер\n'
                'Не стесняйся обращаться ко мне в чатах. Я удалю свой '
                '@username из команды')
        text = text.format(message.from_user.first_name)
        return await message.answer(text, reply_markup=keyboards.menu_kb)
    await message.answer('У тебя нет доступа для использования этого бота.')

# -----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- DONATE--------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="Выдача доната 🍩"))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        await message.answer(text="✍ Введите ник пользователя", reply_markup=keyboards.ext_kb)
        await state.set_state(set_donate.wait_nick)


@dp.message_handler(state=set_donate.wait_nick)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == "Отмена ❌":
        await state.finish()
        await message.answer(text="Действие отменено", reply_markup=keyboards.menu_kb)
    else:
        helper.temp_nick = message.text
        await message.answer(text="Выберите донат 🗒️", reply_markup=keyboards.dn_kb)
        await state.set_state(set_donate.wait_donate_n)


@dp.message_handler(state=set_donate.wait_donate_n)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == "Отмена ❌":
        await state.finish()
        await message.answer(text="Действие отменено", reply_markup=keyboards.menu_kb)
    else:
        helper.temp_donate = message.text
        dotate = helper.definition_butt()
        if dotate == "err":
            await message.answer(text="Неправильный ввод. Выберите донат ИЗ СПИСКА 🗒️", reply_markup=keyboards.dn_kb)
            await state.set_state(set_donate.wait_donate_n)
        else:
            command = "lp user " + helper.temp_nick + " parent set " + dotate
            with MCRcon(config.rcon_host, config.rcon_pass, config.rcon_port) as mcr:
                resp = mcr.command(command)
                logger.info(resp)
            await message.answer(text="Успех ✅", reply_markup=keyboards.menu_kb)
            await state.finish()

# -----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- UPD BALLANCE -------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="Выдача валюты игроку 💵"))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        await message.answer(text="✍ Введите ник пользователя", reply_markup=keyboards.ext_kb)
        await state.set_state(set_donate.wait_nick_to_pay)


@dp.message_handler(state=set_donate.wait_nick_to_pay)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == "Отмена ❌":
        await state.finish()
        await message.answer(text="Действие отменено", reply_markup=keyboards.menu_kb)
    else:
        helper.temp_nick = message.text
        await message.answer(text="Введите сумму пополнения 🤑", reply_markup=keyboards.ext_kb)
        await state.set_state(set_donate.wait_money)


@dp.message_handler(state=set_donate.wait_money)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == "Отмена ❌":
        await state.finish()
        await message.answer(text="Действие отменено", reply_markup=keyboards.menu_kb)
    else:
        if message.text.isnumeric():
            command = "eco give " + helper.temp_nick + " " + message.text
            with MCRcon(
                    config.rcon_host,
                    config.rcon_pass,
                    config.rcon_port
            ) as mcr:
                resp = mcr.command(command)
                logger.info(resp)
            await message.answer(text="Успех ✅ \nИгроку " + helper.temp_nick + " было выдано " + message.text + " $", reply_markup=keyboards.menu_kb)
            await state.finish()
        else:
            await message.answer(text="Неправильный ввод. Введите сумму цифрами 🤑", reply_markup=keyboards.ext_kb)
            await state.set_state(set_donate.wait_money)

# -----------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------  BAN  --------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="Забанить игрока ⛔️"))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        await message.answer(text="✍ Введите ник пользователя (через пробел причину бана, не обязательно)", reply_markup=keyboards.ext_kb)
        await state.set_state(set_donate.wait_ban)


@dp.message_handler(state=set_donate.wait_ban)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == "Отмена ❌":
        await state.finish()
        await message.answer(text="Действие отменено", reply_markup=keyboards.menu_kb)
    else:
        command = "ban " + message.text
        with MCRcon(
                config.rcon_host,
                config.rcon_pass,
                config.rcon_port
        ) as mcr:
            resp = mcr.command(command)
            logger.info(resp)
        await message.answer(text="Игрок забанен ⛔️", reply_markup=keyboards.menu_kb)
        await state.finish()

# -----------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------- PARDON --------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="Разбанить игрока ✅"))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        await message.answer(text="✍ Введите ник пользователя ", reply_markup=keyboards.ext_kb)
        await state.set_state(set_donate.wait_unban)


@dp.message_handler(state=set_donate.wait_unban)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == "Отмена ❌":
        await state.finish()
        await message.answer(text="Действие отменено", reply_markup=keyboards.menu_kb)
    else:
        command = "pardon " + message.text
        with MCRcon(
                config.rcon_host,
                config.rcon_pass,
                config.rcon_port
        ) as mcr:
            resp = mcr.command(command)
            logger.info(resp)
        await message.answer(text="Игрок " + message.text + " разбанен ✅", reply_markup=keyboards.menu_kb)
        await state.finish()

# -----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- RESTART --------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="Перезапустить сервер 🔄"))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        command = "reload"
        with MCRcon(
                config.rcon_host,
                config.rcon_pass,
                config.rcon_port
        ) as mcr:
            resp = mcr.command(command)
            logger.info(resp)
        await message.answer(text="⚠️ ВЫ УВЕРЕНЫ ЧТО ХОТИТЕ ПЕРЕЗАГРУЗИТЬ СЕРВЕР? ⚠️", reply_markup=keyboards.rld_kb)
        await state.set_state(set_donate.wait_reload)


@dp.message_handler(state=set_donate.wait_reload)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == "Отмена 🟢":
        await state.finish()
        await message.answer(text="Действие отменено", reply_markup=keyboards.menu_kb)
    elif message.text == "Да, хочу перезагрузить 🔴":
        command = "reload confirm"
        await message.answer(text="Сервер перезагрузился 🕐", reply_markup=keyboards.menu_kb)
        await state.finish()
        with MCRcon(config.rcon_host, config.rcon_pass, config.rcon_port) as mcr:
            resp = mcr.command(command)
            logger.info(resp)
    else:
        await state.finish()
        await message.answer(text="Действие отменено", reply_markup=keyboards.menu_kb)

# -----------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------- OTHER COMMAND -----------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler()
async def text(message: types.Message):
    if message.from_user.id in config.admins_list:
        bot = await message.bot.get_me()
        command = message.text.replace('@ ' + bot.username, '')
        command = message.text.replace('@' + bot.username, '')
        if command[0] == '/':
            command = command[1:]
        with MCRcon(
                config.rcon_host,
                config.rcon_pass,
                config.rcon_port
        ) as mcr:
            resp = mcr.command(command)
            logger.info(resp)
            i = 0
            while i < len(helper.rm_smb):
                resp = resp.replace(helper.rm_smb[i], ' ')
                i += 1
            await message.reply('<code>%s</code>' % resp)

# -----------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------  POLLING MODE -----------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    executor.start_polling(dp)
