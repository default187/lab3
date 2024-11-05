# Используем официальный базовый образ Python
FROM python:3.10

# Копируем файлы проекта в контейнер
WORKDIR /app
COPY . /app

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Запускаем приложение
CMD ["python", "app.py"]
