from aiogram.fsm.state import StatesGroup, State


class OrderSteps(StatesGroup):
    GET_NAME = State()
    GET_NUMBER = State()
