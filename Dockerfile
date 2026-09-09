FROM python:3.12

RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Santiago
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "server-test/server-opc-general.py"]