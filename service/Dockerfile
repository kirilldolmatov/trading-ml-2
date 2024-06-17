FROM joyzoursky/python-chromedriver:3.8


COPY requirements.txt .

RUN pip install -r requirements.txt

COPY lib ./lib
COPY bot.py bot.py
COPY saved_models ./saved_models

EXPOSE 8000

CMD [ "python", "bot.py"]