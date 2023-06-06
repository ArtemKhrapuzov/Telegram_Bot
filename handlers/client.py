from aiogram import types, Dispatcher
from create_bot import dp, bot


#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Чем могу помочь?')
        await message.delete()
    except:
        await message.reply('Общение с ботом в ЛС, напишите ему: https://t.me/sport_lifeBot')


#@dp.message_handler(commands=['похудение'.lower()])
async def commands_loss(message: types.Message):
    m = 0
    age = 0
    height = 0
    pol = ''
    await bot.send_message(message.from_user.id, 'Ваш вес?')
    if type(message.text) == int:
        await message.answer(message.from_user.id, message.text * 5)


#@dp.message_handler(commands=['набор'])
async def commands_kit(message: types.Message):
    pass

def register_handlers_clients(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_loss, commands=['похудение'])
    dp.register_message_handler(commands_kit, commands=['набор'])