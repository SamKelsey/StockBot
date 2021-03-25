FROM python:3

ENV PYTHON_ENV dev

COPY requirements.txt .
RUN pip install -r /requirements.txt

COPY ./ .

EXPOSE 8080

CMD [ "python", "stockBot/StockBot.py" ]