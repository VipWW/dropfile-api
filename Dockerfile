FROM python:3.11-alpine

WORKDIR /app
COPY . /app

RUN apk update

RUN pip install .

RUN adduser \
    --disabled-password \
    --no-create-home \
    dropfile

RUN chown -R dropfile:dropfile /app

USER dropfile

EXPOSE 5000

CMD ["python", "-m", "flask", "--app", "/app", "run", "--host", "0.0.0.0", "--port", "5000"]
