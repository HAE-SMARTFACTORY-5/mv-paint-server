FROM python:3.9-slim

COPY . /home/mv-paint-server
WORKDIR /home/mv-paint-server

COPY ./requirements.txt /home/mv-paint-server/requirements.txt

RUN apt-get update
RUN pip install -r requirements.txt

CMD ["python","main.py"]