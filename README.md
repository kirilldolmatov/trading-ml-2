# Годовой студенческий проект команды №1

## Описание проекта

В рамках студенческого проекта разработан сервис, который позволяет пользователю получить актуальную информацию о компании. На основе классификации нескольких последних новостей, выдается оценка новостного фона на сегодняшний день. На основе нескольких последних новостей, выдается краткий пересказ. Сервис реализован как телеграм бот.


## Схема 

![Scheme.](Diagram.jpeg 'Diag')


## Сборка Docker контейнера и Push в Docker Hub

### Сборка


```bash
docker build -t news_predictions:latest . 
```

```bash
docker tag news_predictions:latest news_predictions:latest
```

```bash
docker push news_predictions:latest
```


### Запуск 

```bash
docker run -e BOT_TOKEN="" -d news_predictions:latest
```

### Ссылка на Docker Image

[Docker Image](https://hub.docker.com/r/lytkinvs/news_predictions)