FROM yandex/clickhouse-server

RUN apt update
COPY create_database.sh .
COPY create_media_table.sql .
VOLUME /home/r4wm/hoyj_clickhouse_database:/var/lib/clickhouse
EXPOSE 8123/tcp


