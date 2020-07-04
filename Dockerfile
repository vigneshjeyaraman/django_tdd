# this is the base image with which we are creating our docker.
FROM python:3.7-alpine
MAINTAINER Vignesh Jeyaraman

# this is suggested to do when we are running
# python django with docker
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# This is done to create an user with name user
# it is important because if we don't do this
# then docker will run app using root account
# and if someone comprises our application they will
# have root access and can do anything
# to avoid this we create a separate user with limited
# access so that intruder will have limited access.
RUN adduser -D user
# this will switch the user
USER user 

