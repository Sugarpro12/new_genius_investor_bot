# Используем официальный образ Python как базу
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Команда по умолчанию для запуска бота
CMD ["python", "main.py"]
