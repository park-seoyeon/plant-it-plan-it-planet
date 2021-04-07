FROM python:3.7.7


ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim


RUN mkdir /srv/docker
ADD . /srv/docker

WORKDIR /srv/docker

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

EXPOSE 8000 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
