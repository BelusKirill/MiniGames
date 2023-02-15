import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging = logging.getLogger(__name__)


def keyboard_start_user() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    btn_rsp = InlineKeyboardButton(f'Камень, ножницы, бумага', callback_data='game_rsp')
    keyboard.row(btn_rsp)
    return keyboard

def keyboard_menu_game_rsp() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    btn_online_play = InlineKeyboardButton(f'Играть онлайн', callback_data='rsp_online_pay')
    btn_computer_pay = InlineKeyboardButton(f'Играть с компьютером', callback_data='rsp_computer_pay')
    btn_rules = InlineKeyboardButton(f'Правила', callback_data='rsp_rules')
    keyboard.add(btn_online_play)
    keyboard.add(btn_computer_pay)
    keyboard.add(btn_rules)
    return keyboard
