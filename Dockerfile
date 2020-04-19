FROM python:3.5-alpine

WORKDIR /app

COPY . /app

RUN pip install -r ./app/requirements.txt

EXPOSE 8181

ENTRYPOINT ["python", "./app/server.py"]
