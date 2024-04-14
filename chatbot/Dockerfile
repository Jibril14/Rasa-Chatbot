FROM rasa/rasa:3.6.20-full

WORKDIR /app

# COPY requirements.txt .

# RUN pip install --verbose -r requirements.txt

COPY . .

COPY ./data /app/data

RUN rasa train

EXPOSE 5005

CMD ["run", "-m", "/app/models", "--enable-api", "--cors", "*", "--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]