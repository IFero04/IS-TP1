FROM postgres:15.5-alpine3.18

ENV POSTGRES_USER=is
ENV POSTGRES_PASSWORD=is
ENV POSTGRES_DB=is_rel

COPY schema.sql /docker-entrypoint-initdb.d/

EXPOSE 1002