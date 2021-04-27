FROM postgres:10.5

ENV POSTGRES_PASSWORD=root
ENV POSTGRES_USER=root
ENV POSTGRES_DB=chat

COPY init.sql /docker-entrypoint-initdb.d/init.sql

VOLUME ./postgres-data:/var/lib/postgresql/data

EXPOSE 5432