FROM python:3.8
RUN mkdir /api
WORKDIR /api
COPY requirements.txt /api/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /api/
