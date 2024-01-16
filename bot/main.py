
import asyncio
from aiogram import Bot, Dispatcher, html, types, enums
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from FinamNewsParser import FinamNewsParser
from TextRank import TextRankSummarizer
from tickers import get_tickers
from get_ticker import get_ticker_by_company

BOT_TOKEN = ""

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
tickers, companies = get_tickers()

def get_ticker(ticker: str):
    return get_ticker_by_company(ticker)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Введи тикер или название российской компании новости которой тебя интересуют.")

@dp.message()
async def get_news(message: types.Message):
    ticker = get_ticker(message.text)

    if ticker is None:
        await message.answer("К сожалению, мы не смогли найти вашу компанию. Давайте попробуем другую.")
        return
    
    await message.answer(text=f"Ищем новости по тикеру: <b>{html.quote(ticker.upper())}</b>", parse_mode=ParseMode.HTML)
    
    parser = FinamNewsParser()
    news = parser.collect_news(ticker, maxCount=3)

    if len(news) == 0:
        await message.answer("Мы не смогли найти новости по вашей компании. Давайте поробуем другую.")
    
    await message.answer("Краткий пересказ последних новостей компании, которые нам удалось найти.")
    
    string_builder = []
    
    for article in news:
        text_rank = TextRankSummarizer()
        summary = text_rank(article.text, 3)
        string_builder.append(f"<b>{html.quote(article.title)}, от {html.quote(article.date)}</b>")
        string_builder.append(f"{html.quote(summary)}")
        string_builder.append("\n")

    await message.answer(text="\n".join(string_builder), parse_mode=ParseMode.HTML)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())