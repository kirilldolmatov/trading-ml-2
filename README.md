# trading-ml-2

Годовой студенческий проект команды №1

* Этап 1. Получение данных:
    - [Тинькофф Пульс](/data/Tinkoff/tinkoff_puls.ipynb)
    - [Финам](/data/Finam/README.md)
    - [Московская биржа](/data/MOEX/MOEX.ipynb)
* Этап 2. EDA:



# Сборка Docker контейнера и Push в Docker Hub

## Сборка


```bash
docker build -t news_predictions:latest . 
```

```bash
docker tag news_predictions:latest news_predictions:latest
```

```bash
docker push news_predictions:latest
```


## Запуск 

```bash
docker run -e BOT_TOKEN="" -d news_predictions:latest
```

## Ссылка на Docker Image

[Docker Image](https://hub.docker.com/r/lytkinvs/news_predictions)