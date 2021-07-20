FROM ubuntu:18.04

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install python3.6 python3.6-dev python-dev python3-dev \
    && apt-get -y install python3-pip python-dev

COPY . .

RUN pip3 install -r requirements.txt

WORKDIR /server_core
CMD ["gunicorn" , "--bind" , ":8000" , "--threads" , "50" , "server:app"]

#test
