import asyncio
from aiogram import types
from aiogram.types import Message, ContentType
import random as r
from config import admin_id
from main import bot, dp
from user_id import check_id,open_users
async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Bot is started")

@dp.message_handler(commands=['start'])
async def process_start_command(message):
    text = ('Привет!\nЯ отправлю каждое следующие новые сообщения каждую одному рандомному человеку.\n'
            'Напиши что нибудь - вдруг и тебе напишут!')
    await message.answer(text=text)
    await check_id(message.from_user.id)

@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    audio_id = message.voice.file_id
    caption = message.caption
    users = open_users()
    user = message.from_user.id
    while user == message.from_user.id:
        user = r.choice(list(users))
    await message.answer('Я отправил твое сообщение!')
    await bot.send_message(chat_id=user, text=f"От кого-то пришло сообщение:")
    await bot.send_voice(user, audio_id,
                         caption=caption)

@dp.message_handler(content_types=['photo'])
async def photo_handler(message):
    file_id = message.photo[-1].file_id
    caption = message.caption
    users = open_users()
    user = message.from_user.id
    while user == message.from_user.id:
        user = r.choice(list(users))
    print(user)
    print(message)
    await bot.send_message(chat_id=user, text=f"От кого-то пришло сообщение:")
    await bot.send_photo(user, file_id, caption=caption)
    text = f"Я отправил твое сообщение!"
    await message.answer(text=text)

@dp.message_handler(content_types=['video'])
async def video_handler(message):
    file_id = message.video.file_id
    caption = message.caption
    users = open_users()
    user = message.from_user.id
    while user == message.from_user.id:
        user = r.choice(list(users))
    print(user)
    print(message)
    await bot.send_message(chat_id=user, text=f"От кого-то пришло сообщение:")
    await bot.send_video(user, file_id, caption=caption)
    text = f"Я отправил твое сообщение!"
    await message.answer(text=text)

@dp.message_handler(content_types=['video_note'])
async def video_note_handler(message):
    print(message)
    file_id = message.video_note.file_id
    users = open_users()
    user = message.from_user.id
    while user == message.from_user.id:
        user = r.choice(list(users))
    print(user)
    print(message)
    await bot.send_message(chat_id=user, text=f"От кого-то пришло сообщение:")
    await bot.send_video_note(user, file_id)
    text = f"Я отправил твое сообщение!"
    await message.answer(text=text)

@dp.message_handler(content_types=['sticker'])
async def sticker_handler(message):
    file_id = message.sticker.file_id
    users = open_users()
    user = message.from_user.id
    while user == message.from_user.id:
        user = r.choice(list(users))
    print(user)
    print(message)

    await bot.send_message(chat_id=user, text=f"От кого-то пришло сообщение:")
    await bot.send_sticker(user, file_id)

    text = f"Я отправил твое сообщение!"
    await message.answer(text=text)

@dp.message_handler()
async def echo(message):
    users = open_users()
    user = message.from_user.id
    while user == message.from_user.id:
        user = r.choice(list(users))
    print(user)
    print(message)

    await bot.send_message(chat_id=user, text=f"От кого-то пришло сообщение:")
    await bot.send_message(chat_id=user, text=message.text )


    text = f"Я отправил твое сообщение!"
    await message.answer(text=text)

    #await bot.send_message(chat_id=message.from_user.id, text=text)
