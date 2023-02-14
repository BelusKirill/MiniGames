from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ChatType, CallbackQuery

from loader import bot, db, config
from tgbot.keyboards.inline import keyboard_start_user, keyboard_menu_game_rps


async def user_start(message: Message, state: FSMContext):
    """
    Обработчик команды Start
    Выводит список мини-игр
    Возвращает: None
    """
    await state.finish()
    await message.answer("Список мини игр", reply_markup=keyboard_start_user())

async def menu_game_rps(callback_query: CallbackQuery, state: FSMContext):
    """
    Обработчик меню игры Камень, ножницы, бумага
    Возвращает: None
    """
    await state.finish()
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer("Камень, ножницы, бумага", reply_markup=keyboard_menu_game_rps())


def register_user(dp: Dispatcher):
    """
    Функция регистрирует обработчики и описывает правила 
    вызова обработчиков 
    Возвращает: None
    """
    dp.register_message_handler(user_start, commands=["start"], chat_type=ChatType.PRIVATE, state="*")
    dp.register_callback_query_handler(menu_game_rps, lambda c: c.data and c.data == 'game_rps', chat_type=ChatType.PRIVATE)
