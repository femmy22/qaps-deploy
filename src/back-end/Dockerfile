FROM python:3.8-slim-buster

RUN pip install --upgrade pip && pip install flask

WORKDIR /app

COPY . /app

EXPOSE 5000

RUN pip3 install -r packages.txt

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]