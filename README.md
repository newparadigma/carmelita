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
2. Описание карт.
3. Перевернутые карты.
4. Разные виды предсказаний.
5. Реагирование на тег @carmelita
6. Добавление автодополнения вводимых комманд в чате