FROM postgres:12
COPY ./init/dump1.sql /docker-entrypoint-initdb.d/

RUN chmod -R 775 /docker-entrypoint-initdb.d