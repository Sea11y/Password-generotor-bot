import random
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import InputFile
from loader import dp, bot
from src.states.passwords import PassFSM


def password_gen(length):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = int(length)
    password =''
    for i in range(length):
        password += random.choice(chars)
    return password


@dp.message_handler(Text(equals='Pass', ignore_case = True))
@dp.message_handler(Command("Pass"))
async def bot_start(message : types.Message):
    await message.answer("Привет 👋!\nКакой длины пароль вам нужен?😃\n\n"
                         "Hello 👋!\nHow long is the password you need?😃\n\n")
    await PassFSM.get_length.set()


@dp.message_handler(state=PassFSM.get_length)
async def sending_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lenght'] = message.text
    try:
        async with state.proxy() as data:
            data['length'] = message.text
        set_length = data['length']
        ready_pass = password_gen(set_length)
        await message.answer(f'{ready_pass} - Password 😃\n\n'
                             f'🤗Хорошего дня!🤗\n'
                             f'🤗Have a god day!🤗')
    except:
        await message.answer('😵Произошла ошибка😵\n\n'
                             '😵An error has occurred😵')
    await state.finish()

