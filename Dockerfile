FROM python:3.6-alpine
WORKDIR /FASTFOOD-FLASK
COPY . /FASTFOOD-FLASK
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0"]
