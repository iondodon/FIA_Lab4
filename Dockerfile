FROM python:3.8.5

COPY . /var/www/server
WORKDIR /var/www/server

RUN pip install -r requirements.txt

ENV FLASK_APP server.py
CMD flask run --host=0.0.0.0

EXPOSE 5000

