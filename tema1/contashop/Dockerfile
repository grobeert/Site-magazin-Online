FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p submitted-orders

EXPOSE 5000

CMD ["python3", "server.py"]
