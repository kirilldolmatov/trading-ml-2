import asyncio
from aiogram import Bot, Dispatcher, html, types, enums
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

from bot.FinamNewsParser import FinamNewsParser
from bot.TextRank import TextRankSummarizer
import pickle

# from bot import TextRankSummarizer
# from bot import get_tickers
# from bot import get_ticker_by_company
#
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def lr_model_predictor(news):
    with open('tfidf.pickle', 'rb') as file:
        tfidf = pickle.load(file)

    with open('lr_clf.pickle', 'rb') as file:
        lr_clf = pickle.load(file)

    X = tfidf.transform([news])

    lr_pred = lr_clf.predict(X)

    lr_pred_proba = lr_clf.predict_proba(X)

    return (lr_pred, lr_pred_proba)

def test():
    ticker = "SBER"

    if ticker is None:
        return

    print("Ищем новости по тикеру: <b>{html.quote(ticker.upper())}</b>")

    parser = FinamNewsParser()
    news = parser.collect_news(ticker, maxCount=3)

    if len(news) == 0:
        print("Мы не смогли найти новости по вашей компании. Давайте поробуем другую.")

    print("Краткий пересказ последних новостей компании, которые нам удалось найти.")

    string_builder = []
    print(len(news))
    for article in news:
        print(article.text)
        print(article.date)
        lr_pred, lr_pred_proba = lr_model_predictor(article.text)
        print(lr_pred)
        print(lr_pred_proba)
        
        print("----")
        


test()
