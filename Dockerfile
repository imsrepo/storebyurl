FROM python:3.9-alpine

WORKDIR /app

COPY . /app/

RUN pip install -r requirments.txt

EXPOSE 5000

CMD python ./app.py

