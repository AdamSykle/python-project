# Используем официальный образ Python
FROM python:3.12.2

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Открываем порт для приложения
EXPOSE 5000

# Запуск приложения
CMD ["python", "app.py"]
