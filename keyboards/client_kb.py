from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b1 = KeyboardButton('Похудение')
b2 = KeyboardButton('Набор')
#b3 = KeyboardButton('Поделиться номером', request_contact=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).insert(b2)#.row(b3)


