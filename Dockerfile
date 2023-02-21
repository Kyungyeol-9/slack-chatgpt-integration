FROM python:3.10-bullseye

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "slack.py"]