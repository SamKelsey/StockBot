FROM python:3

COPY ./ .

CMD [ "python", "stockBot/stockBot.py" ]