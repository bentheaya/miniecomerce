FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8001
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8001 user.wsgi:application"]