# bot.py
import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import logging
from rag import retrieve_top_k, generate_answer, load_index_from_pdfs


load_dotenv()
BOT_TOKEN = os.getenv("SONUN_TOKEN")


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

# Load index on startup
pdf_files = ["sonun.pdf"]
index, text_chunks = load_index_from_pdfs(pdf_files)


@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("Welcome! Ask me anything about Sonun University 📚")


@dp.message(F.text)
async def handle_question(message: Message):
    question = message.text
    top_chunks = retrieve_top_k(question, index, text_chunks)
    context = "\n\n".join(top_chunks)
    answer = generate_answer(question, context, use_ollama=True)
    await message.answer(answer)
    
@dp.message(F.text)
async def handle_question(message: Message):
    print("Received:", message.text)
    ...

    


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
