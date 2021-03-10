FROM python:3.9-slim-buster
WORKDIR .
EXPOSE 8080

COPY . .
RUN pip3 install -r requirements.txt


CMD [ "python3", "main.py"]