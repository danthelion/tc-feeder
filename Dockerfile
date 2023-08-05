FROM ubuntu:latest

RUN apt update && \
    apt install python3 python3-pip -y && \
    pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
