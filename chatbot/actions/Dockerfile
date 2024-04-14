FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --verbose -r requirements.txt

COPY . .

EXPOSE 5055

USER 1001