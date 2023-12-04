FROM postgres:9.6.5

ENV POSTGRES_USER=is
ENV POSTGRES_PASSWORD=is
ENV POSTGRES_DB=is_xml

COPY schema.sql /docker-entrypoint-initdb.d/

EXPOSE 1001