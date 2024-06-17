from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

from lib.FinamNewsParser import FinamNewsParser
from lib.TextRank import TextRankSummarizer

print("start parser")
parser = FinamNewsParser()
news = parser.collect_news("SBER", maxCount=3)

string_builder = []

for article in news:
    text_rank = TextRankSummarizer()

    print(article.text)
    summary = text_rank(article.text, 3)
    print("-----")
    print(summary)
    print("--------------------")
    # string_builder.append(summary)

# print("\n".join(string_builder))