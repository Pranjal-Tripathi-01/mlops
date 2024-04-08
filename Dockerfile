
FROM apache/airflow:2.8.4

USER root
COPY dataset .

RUN apt-get update && \
    apt-get install -y python3-dev python3-pip libffi-dev libssl-dev libcairo2 libcairo2-dev libgirepository1.0-dev pkg-config libgl1-mesa-dev && \
    rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER airflow

