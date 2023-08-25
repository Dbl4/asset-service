FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY app ./

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
