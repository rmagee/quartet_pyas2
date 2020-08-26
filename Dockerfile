FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update -y
RUN apt-get install g++ -y
RUN apt-get install libpcre3 libpcre3-dev -y
RUN apt-get install build-essential -y
RUN apt-get install python-dev -y
RUN apt-get install python-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install openssl -y
RUN apt-get install automake -y
RUN apt-get install git -y
RUN apt-get install bison flex -y
RUN git clone https://github.com/swig/swig.git
RUN . swig/autogen.sh
RUN . swig/configure
COPY requirements.txt /code/
#RUN pip install -r requirements.txt
COPY . /code/