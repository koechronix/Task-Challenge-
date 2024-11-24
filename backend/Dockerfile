FROM python:3.7

RUN export export FLASK_APP=main.py
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

CMD [ "python", "flask run" ]
