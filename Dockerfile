FROM python:3.6
WORKDIR /fastfood-flask
COPY . /fastfood-flask
RUN pip install -r requirements.txt
ENV FLASK_APP=app
ENV FLASK_ENV=development
