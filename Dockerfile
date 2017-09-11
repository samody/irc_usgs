FROM python:2.7
ADD bot.py /
ADD irc.py /
ADD pull.py /

RUN pip install requests

CMD [ "python", "./bot.py" ]



