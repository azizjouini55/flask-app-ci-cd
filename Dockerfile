FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

ENV HOST=0.0.0.0

EXPOSE 5000

CMD [ "python3", "./app.py"]
