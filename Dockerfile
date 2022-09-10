FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3.9 python3.9-dev && \
    apt-get install -y python3-pip && \
    apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    wget https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["behave"]