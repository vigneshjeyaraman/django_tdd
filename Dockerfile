# this is the base image with which we are creating our docker.
FROM python:3.7-alpine
LABEL Vignesh Jeyaraman

# this is suggested to do when we are running
# python django with docker
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# below these are dependency for psycopg2
# what we did is to keep our docker container light
# we installed those dependency and later once psycopg is
# installed we will delete them.
# musl and zlib are dependencies for pillow
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

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
# -p will create directory and subdirectory if they don't
# exists
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
# given user permission for vol folder
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
# this will switch the user
USER user 

