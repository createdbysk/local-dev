FROM python:3.8.6-buster

WORKDIR /app

COPY requirements.txt .
COPY src/ .

RUN pip install -r requirements.txt --upgrade

ENTRYPOINT ["python", "app.py"]
