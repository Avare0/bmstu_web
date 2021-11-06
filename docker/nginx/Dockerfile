FROM nginx:latest
RUN apt-get update
RUN apt-get install -y nginx-extras
RUN mkdir /var/cache/nginx
COPY nginx.conf /etc/nginx/nginx.conf