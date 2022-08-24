from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(Text(equals='start', ignore_case = True))
@dp.message_handler(CommandStart(), state="*")
async def start(message: types.Message):
    await message.answer(f"Hello 👋, {message.from_user.full_name}!\n\n"
                         f"Start using the bot: /Pass")




