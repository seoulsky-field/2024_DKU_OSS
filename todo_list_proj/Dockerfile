FROM python:3.10

MAINTAINER Wimes <yeon2002.kj@dankook.ac.kr> 

RUN pip install Django

COPY . .

EXPOSE 7777

CMD ["python", "manage.py", "runserver", "0.0.0.0:7777"]
