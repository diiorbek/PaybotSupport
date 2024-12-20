from aiogram.fsm.state import State, StatesGroup

class AdminMessage(StatesGroup):
    user_id = State()
    text = State()
