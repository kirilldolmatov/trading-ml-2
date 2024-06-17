import asyncio

from aiogram import Bot, Dispatcher, html, types, enums, F
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lib.FinamNewsParser import FinamNewsParser
from lib.TextRank import TextRankSummarizer
from lib.get_ticker import get_ticker_by_company, get_ticker_by_company_two
from lib.DLModel import load_model, predict_news
import pickle
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
print(BOT_TOKEN)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_ticker(ticker):
    return get_ticker_by_company_two(ticker)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Введи тикер или название российской компании " +
                         "новости которой тебя интересуют.")


@dp.message()
async def get_news(message: types.Message):
    ticker = get_ticker(message.text)
    print(ticker)
    if ticker is None:
        await message.answer("К сожалению, мы не смогли найти вашу компанию. " +
                             "Давайте попробуем другую.")
        return

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Краткий пересказ новостей",
        callback_data="ticker_nw_" + ticker)
    )
    builder.row(types.InlineKeyboardButton(
        text="Новостной фон (ML - модель)",
        callback_data="ticker_ml_" + ticker)
    )
    builder.row(types.InlineKeyboardButton(
        text="Новостной фон (DL - модель)",
        callback_data="ticker_dl_" + ticker),
    )

    await message.answer(
        f"Информация по тикеру <b>{html.quote(ticker.upper())}</b>",
        reply_markup=builder.as_markup(),
        parse_mode=ParseMode.HTML
    )


@dp.callback_query(F.data.startswith("ticker_"))
async def send_random_value(callback: types.CallbackQuery):
    splitted_txt = callback.data.split("_")
    ticker = splitted_txt[2]
    command_type = splitted_txt[1]
    if command_type == 'nw':
        await news_parser(ticker, callback.message.answer)
    if command_type == 'ml':
        await ml_prediction(ticker, callback.message.answer)
    if command_type == 'dl':
        await dl_prediction(ticker, callback.message.answer)


async def news_parser(ticker, callback):
    await callback(text=f"Ищем новости по тикеру: <b>{html.quote(ticker.upper())}</b>",
                   parse_mode=ParseMode.HTML)

    parser = FinamNewsParser()
    news = parser.collect_news(ticker, maxCount=3)

    if len(news) == 0:
        await callback("Мы не смогли найти новости по вашей компании. Давайте поробуем другую.")

    await callback("Краткий пересказ последних новостей компании, которые нам удалось найти.")

    string_builder = []
    
    for article in news:
        text_rank = TextRankSummarizer()
        try:
            summary = text_rank(article.text, 3)
            string_builder.append(f"<b>{html.quote(article.title)}, от {html.quote(article.date)}</b>")
            string_builder.append(f"{html.quote(summary)}")
            string_builder.append("\n")
        except Exception:
            pass

    await callback(text="\n".join(string_builder), parse_mode=ParseMode.HTML)


async def ml_prediction(ticker, callback):
    await callback(text=f"Формируем новостной фон по тикеру: <b>{html.quote(ticker.upper())}</b>",
                   parse_mode=ParseMode.HTML)

    parser = FinamNewsParser()
    news = parser.collect_news(ticker, maxCount=4)

    with open('./saved_models/ml/tfidf.pickle', 'rb') as file:
        tfidf = pickle.load(file)

    with open('./saved_models/ml/lr_clf.pickle', 'rb') as file:
        lr_clf = pickle.load(file)

    X = tfidf.transform([article.text for article in news])

    lr_pred = lr_clf.predict(X)

    lr_pred_proba = lr_clf.predict_proba(X)

    add_proba = [1 if pred[1] > 0.6 else 0 for pred in lr_pred_proba]
    print(add_proba)
    st = (f"На сегодняшний день, новостной фон компании "
          f"составляет <b>{sum(add_proba)}/{len(add_proba)}</b> баллов")
   
    await callback(text=st, parse_mode=ParseMode.HTML)


async def dl_prediction(ticker, callback):
    await callback(text=f"Формируем новостной фон по тикеру: <b>{html.quote(ticker.upper())}</b>",
                   parse_mode=ParseMode.HTML)

    model, tokenizer = load_model('./saved_models/dl/checkpoint.pth')

    parser = FinamNewsParser()
    news = parser.collect_news(ticker, maxCount=4)

    predictions = []

    for article in news:
        lable, pred_proba = predict_news(model, tokenizer, article.text)
        predictions.append(lable)

    st = (f"На сегодняшний день, новостной фон компании "
          f"составляет <b>{sum(predictions)}/{len(predictions)}</b> баллов")
    print(st)
    await callback(text=st, parse_mode=ParseMode.HTML)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
