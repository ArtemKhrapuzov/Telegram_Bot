from aiogram import types, Dispatcher
import json, string
from create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('маты.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()
    if message.text.lower() == 'привет':
        await message.reply('И тебе привет!!')


def register_handlers_clients(dp: Dispatcher):
    dp.register_message_handler(echo_send)
