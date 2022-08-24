from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(Text(equals='start', ignore_case = True))
@dp.message_handler(CommandHelp(), state="*")
async def show_info(message: types.Message):
    await message.answer('📍 In order to start using the bot: /Pass\n', disable_web_page_preview=True)
