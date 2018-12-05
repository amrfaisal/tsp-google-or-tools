FROM python:stretch
WORKDIR /usr/app

RUN pip install -U ortools

COPY . .
CMD ["python", "main.py" ]