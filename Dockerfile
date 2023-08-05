FROM ubuntu:latest

WORKDIR /app

RUN apt update && \
    apt install python3 python3-pip wget unzip curl -y

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -  && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'  && \
    apt update && \
    apt install -y google-chrome-stable

RUN apt-get install -yqq unzip && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

ENV DISPLAY=:99

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "/app/main.py"]
