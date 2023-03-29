from pytube import YouTube
from aiogram import Dispatcher, Bot, types, executor
import os
import logging
# Configure logging
logging.basicConfig(level=logging.INFO)


bot = Bot("")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
    await message.answer( "Привіт я можу завантажити відео з YouTube\n"
                                   "Відправ мені лінк на відео")

@dp.message_handler()
async  def text_message(message:types.Message):
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
        await message.answer_chat_action("UPLOAD_VIDEO")
        await message.answer( f"*Починаю завантажувати відео*: {yt.title}\n"
                                       f" *З Канала* : [{yt.author}]({yt.channel_url})", parse_mode="Markdown")
        await downloand_youtube_video(url, message, bot)

async def downloand_youtube_video(url,message,bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    print(stream.all())
    stream.get_lowest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as video:
        await message.answer_video( video, caption="*Завантаження завершено. Гарного перегляду*", parse_mode="Markdown")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
