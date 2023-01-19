from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from config import Configuration
from mcrcon import MCRcon
import logging
import locale
import helper

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
        text = locale.start_message_ok.format(message.from_user.first_name)
        return await message.answer(text, reply_markup=helper.menu_kb)
    await message.answer(locale.start_message_err)

# -----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- DONATE--------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals=locale.get_donate_btn))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        await message.answer(text=locale.input_nick, reply_markup=helper.ext_kb)
        await state.set_state(set_donate.wait_nick)


@dp.message_handler(state=set_donate.wait_nick)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == locale.cancel_btn:
        await state.finish()
        await message.answer(text=locale.cancel_ok, reply_markup=helper.menu_kb)
    else:
        helper.temp_nick = message.text
        helper.kbd_gen()
        await message.answer(text=locale.choose_donate, reply_markup=helper.dn_kb)
        await state.set_state(set_donate.wait_donate_n)


@dp.message_handler(state=set_donate.wait_donate_n)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == locale.cancel_btn:
        await state.finish()
        await message.answer(text=locale.cancel_ok, reply_markup=helper.menu_kb)
    else:
        helper.temp_donate = message.text
        donate = helper.definition_butt()
        if donate == "err":
            await message.answer(text=locale.err_choose_donate, reply_markup=helper.dn_kb)
            await state.set_state(set_donate.wait_donate_n)
        else:
            command = "lp user " + helper.temp_nick + " parent set " + donate
            with MCRcon(config.rcon_host, config.rcon_pass, config.rcon_port) as mcr:
                resp = mcr.command(command)
                logger.info(resp)
            await message.answer(text=locale.success, reply_markup=helper.menu_kb)
            await state.finish()

# -----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- UPD BALLANCE -------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals=locale.issuance_currency_btn))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        await message.answer(text=locale.input_nick, reply_markup=helper.ext_kb)
        await state.set_state(set_donate.wait_nick_to_pay)


@dp.message_handler(state=set_donate.wait_nick_to_pay)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == locale.cancel_btn:
        await state.finish()
        await message.answer(text=locale.cancel_ok, reply_markup=helper.menu_kb)
    else:
        helper.temp_nick = message.text
        await message.answer(text=locale.input_amount, reply_markup=helper.ext_kb)
        await state.set_state(set_donate.wait_money)


@dp.message_handler(state=set_donate.wait_money)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == locale.cancel_btn:
        await state.finish()
        await message.answer(text=locale.cancel_ok, reply_markup=helper.menu_kb)
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
            await message.answer(text=locale.success + message.text + " $", reply_markup=helper.menu_kb)
            await state.finish()
        else:
            await message.answer(text=locale.err_input_amount, reply_markup=helper.ext_kb)
            await state.set_state(set_donate.wait_money)

# -----------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------  BAN  --------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals=locale.ban_btn))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        await message.answer(text=locale.input_nick_ban, reply_markup=helper.ext_kb)
        await state.set_state(set_donate.wait_ban)


@dp.message_handler(state=set_donate.wait_ban)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == locale.cancel_btn:
        await state.finish()
        await message.answer(text=locale.cancel_ok, reply_markup=helper.menu_kb)
    else:
        command = "ban " + message.text
        with MCRcon(
                config.rcon_host,
                config.rcon_pass,
                config.rcon_port
        ) as mcr:
            resp = mcr.command(command)
            logger.info(resp)
        await message.answer(text=locale.ban_ok, reply_markup=helper.menu_kb)
        await state.finish()

# -----------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------- PARDON --------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals=locale.pardon_btn))
async def with_puree(message: types.Message, state: FSMContext):
    if message.from_user.id in config.admins_list:
        await message.answer(text=locale.input_nick, reply_markup=helper.ext_kb)
        await state.set_state(set_donate.wait_unban)


@dp.message_handler(state=set_donate.wait_unban)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == locale.cancel_btn:
        await state.finish()
        await message.answer(text=locale.cancel_ok, reply_markup=helper.menu_kb)
    else:
        command = "pardon " + message.text
        with MCRcon(
                config.rcon_host,
                config.rcon_pass,
                config.rcon_port
        ) as mcr:
            resp = mcr.command(command)
            logger.info(resp)
        await message.answer(text=locale.pardon_ok, reply_markup=helper.menu_kb)
        await state.finish()

# -----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- RESTART --------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals=locale.restart_btn))
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
        await message.answer(text=locale.rst_warning, reply_markup=helper.rld_kb)
        await state.set_state(set_donate.wait_reload)


@dp.message_handler(state=set_donate.wait_reload)
async def amount_set(message: types.Message, state: FSMContext):
    if message.text == locale.cancel_rst_btn:
        await state.finish()
        await message.answer(text=locale.cancel_ok, reply_markup=helper.menu_kb)
    elif message.text == locale.run_rst_btn:
        command = "reload confirm"
        await message.answer(text=locale.rst_ok, reply_markup=helper.menu_kb)
        await state.finish()
        with MCRcon(config.rcon_host, config.rcon_pass, config.rcon_port) as mcr:
            resp = mcr.command(command)
            logger.info(resp)
    else:
        await state.finish()
        await message.answer(text=locale.cancel_ok, reply_markup=helper.menu_kb)

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
