FROM python:3.9-alpine

WORKDIR /app

ADD job.py /app/job.py

RUN chmod +x /app/job.py

ENTRYPOINT ["python3", "/app/job.py"]
