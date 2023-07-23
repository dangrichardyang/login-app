FROM python:3.9-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000", "--root-path=/login/api" ]
