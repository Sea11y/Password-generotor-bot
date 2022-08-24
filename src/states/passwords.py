from aiogram.dispatcher.filters.state import StatesGroup, State


class PassFSM(StatesGroup):
    get_length = State()