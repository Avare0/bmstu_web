FROM python:3.8
RUN mkdir /django
WORKDIR /django
COPY requirements.txt /django/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /django/
