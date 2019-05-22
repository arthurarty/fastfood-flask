FROM python:3.6
WORKDIR /FASTFOOD-FLASK
COPY . /FASTFOOD-FLASK
RUN pip install -r requirements.txt
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
