# carmelita
A telegram bot predicting the future by tarot cards.

# Инструкция по установке
1. Копируем docker-compose инструкцию:
```bash
cp docker-compose.example.yml docker-compose.yml
```
2. Копируем переменные окружения:
```bash
cp example.env .env
```
3. Заполните переменные окружения в файле .env!
4. Строим контейнеры
```bash
docker-compose build
```
5. Запускаем контейнеры
```bash
docker-compose up -d
```


# to-do
1. Генерация предсказаний.
2. Защита от перебора предсказаний - 1 предсказание на пользователя раз в день. (Колоде нужно отдохнуть)
3. Реакция бота на тег