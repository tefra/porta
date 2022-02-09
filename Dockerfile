FROM python:3.10

WORKDIR /app

RUN pip install -U pip pip-tools

COPY requirements/base.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["make", "start"]
