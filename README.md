# hoyj_clickhouse

``` bash
docker build -t hoyj_clickhouse .
docker image ls
docker run -it -d -p 8123:8123 --ulimit nofile=262144:262144 --volume=$HOME/hoyj_clickhouse_database:/var/lib/clickhouse f6bb0319508e

```

example
```
[r4wm@todo hoyj_clickhouse]$ docker run -it -d -p 8123:8123 --ulimit nofile=262144:262144 --volume=$HOME/hoyj_clickhouse_database:/var/lib/clickhouse f6bb0319508e
01a1ea216bf9130e8ec932be9c5de73eafd51480fb7e80c3d9a1b78509b6cd92
[r4wm@todo hoyj_clickhouse]$ docker container ls 
CONTAINER ID   IMAGE          COMMAND            CREATED         STATUS         PORTS                                                           NAMES
01a1ea216bf9   f6bb0319508e   "/entrypoint.sh"   6 seconds ago   Up 5 seconds   9000/tcp, 0.0.0.0:8123->8123/tcp, :::8123->8123/tcp, 9009/tcp   confident_joliot
[r4wm@todo hoyj_clickhouse]$ curl http://localhost:8123
Ok.
[r4wm@todo hoyj_clickhouse]$ 


[r4wm@todo hoyj_clickhouse]$ 
[r4wm@todo hoyj_clickhouse]$ ./01_create_workspace.sh 
+ rm -rf /home/r4wm/hoyj_clickhouse_database
+ mkdir /home/r4wm/hoyj_clickhouse_database
[r4wm@todo hoyj_clickhouse]$ docker build -t hoyj:20230106 . 
Sending build context to Docker daemon  69.12kB
Step 1/6 : FROM yandex/clickhouse-server
 ---> c739327b5607
Step 2/6 : RUN apt update
 ---> Running in c187f32046cc

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Get:1 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]
Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
Get:3 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
Get:4 http://archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]
Ign:5 https://repo.clickhouse.com/deb/stable main/ InRelease
Get:6 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages [1,275 kB]
Get:7 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [27.7 kB]
Get:8 http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages [11.3 MB]
Get:9 https://repo.clickhouse.com/deb/stable main/ Release [749 B]
Get:10 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [2,368 kB]
Get:11 https://repo.clickhouse.com/deb/stable main/ Release.gpg [836 B]
Get:12 https://repo.clickhouse.com/deb/stable main/ Packages [230 kB]
Get:13 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [976 kB]
Get:14 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [1,791 kB]
Get:15 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 Packages [177 kB]
Get:16 http://archive.ubuntu.com/ubuntu focal/restricted amd64 Packages [33.4 kB]
Get:17 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [31.3 kB]
Get:18 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [1,929 kB]
Get:19 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [2,859 kB]
Get:20 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1,277 kB]
Get:21 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [28.6 kB]
Get:22 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 Packages [55.2 kB]
Fetched 25.0 MB in 8s (3,048 kB/s)
Reading package lists...
Building dependency tree...
Reading state information...
70 packages can be upgraded. Run 'apt list --upgradable' to see them.
Removing intermediate container c187f32046cc
 ---> 2d9fb279e652
Step 3/6 : COPY create_database.sh .
 ---> 01c93453f87b
Step 4/6 : COPY create_media_table.sql .
 ---> f7f18c93fd9c
Step 5/6 : VOLUME /home/r4wm/hoyj_clickhouse_database:/var/lib/clickhouse
 ---> Running in 3a7edccd5507
Removing intermediate container 3a7edccd5507
 ---> f93fc6dc0060
Step 6/6 : EXPOSE 8123/tcp
 ---> Running in 402829214e23
Removing intermediate container 402829214e23
 ---> 0e8dd05acc11
Successfully built 0e8dd05acc11
Successfully tagged hoyj:20230106
[r4wm@todo hoyj_clickhouse]$ 
[r4wm@todo hoyj_clickhouse]$ 
[r4wm@todo hoyj_clickhouse]$ 
[r4wm@todo hoyj_clickhouse]$ 
[r4wm@todo hoyj_clickhouse]$ docker image ls 
REPOSITORY                     TAG        IMAGE ID       CREATED         SIZE
hoyj                           20230106   0e8dd05acc11   9 seconds ago   867MB
clickhouse/clickhouse-server   latest     3bbe3275fe85   3 weeks ago     910MB
ubuntu                         20.04      d5447fc01ae6   4 weeks ago     72.8MB
yandex/clickhouse-server       latest     c739327b5607   11 months ago   826MB
[r4wm@todo hoyj_clickhouse]$ docker run -it -d -p 8123:8123 --ulimit nofile=262144:262144 --volume=$HOME/hoyj_clickhouse_database:/var/lib/clickhouse 0e8dd05acc11
80242fc290bc6ce090a7928173afb35c99035e0bfc5d0be7a8ed2428379fbea9
[r4wm@todo hoyj_clickhouse]$ ll      
total 56
drwxr-xr-x 3 r4wm users 4096 Jan  5 23:49 .
drwxr-xr-x 8 r4wm users 4096 Jan  5 23:25 ..
drwxr-xr-x 8 r4wm users 4096 Jan  5 23:33 .git
-rwxr-xr-x 1 r4wm users   94 Jan  5 23:27 01_create_workspace.sh
-rw-r--r-- 1 r4wm users  183 Jan  5 23:39 Dockerfile
-rw-r--r-- 1 r4wm users  269 Jan  5 23:38 Dockerfile~
-rw-r--r-- 1 r4wm users  913 Jan  5 23:33 README.md
-rwxr-xr-x 1 r4wm users  139 Jan  5 23:25 create_database.sh
-rwxr-xr-x 1 r4wm users  130 Jan  5 23:25 create_database.sh~
-rwxr-xr-x 1 r4wm users  371 Jan  5 23:25 create_media_table.sql
-rwxr-xr-x 1 r4wm users  265 Jan  5 23:25 create_media_table.sql~
-rwxr-xr-x 1 r4wm users  119 Jan  5 23:47 remove_containers.sh
-rwxr-xr-x 1 r4wm users  122 Jan  5 23:46 remove_containers.sh~
-rwxr-xr-x 1 r4wm users   32 Jan  5 23:49 show_containers.sh
[r4wm@todo hoyj_clickhouse]$ ./show_containers.sh 
CONTAINER ID   IMAGE          COMMAND            CREATED          STATUS          PORTS                                                           NAMES
80242fc290bc   0e8dd05acc11   "/entrypoint.sh"   14 seconds ago   Up 13 seconds   9000/tcp, 0.0.0.0:8123->8123/tcp, :::8123->8123/tcp, 9009/tcp   boring_aryabhata
[r4wm@todo hoyj_clickhouse]$ docker exec -it 80242fc290bc /bin/bash
root@80242fc290bc:/# ./create_database.sh 
+ echo 'CREATE DATABASE IF NOT EXISTS hoyj ENGINE = Memory COMMENT '\''hoyj media search engine'\'';'
+ clickhouse-client -mn
root@80242fc290bc:/# cat create_media_table.sql | clickhouse-client -mn -dhoyj
root@80242fc290bc:/# 
root@80242fc290bc:/# 
root@80242fc290bc:/# 
root@80242fc290bc:/# clickhouse-client -dhoyj
ClickHouse client version 22.1.3.7 (official build).
Connecting to database hoyj at localhost:9000 as user default.
Connected to ClickHouse server version 22.1.3 revision 54455.

80242fc290bc :) show tables 

SHOW TABLES

Query id: 898cbf35-fdf4-47ab-80dc-a7b126cc7497

┌─name──┐
│ media │
└───────┘

1 rows in set. Elapsed: 0.012 sec. 

80242fc290bc :) desc media 

DESCRIBE TABLE  media

Query id: 730896a3-d2be-4b0a-aca0-fa0e2445454f

┌─name────────────────┬─type───┬─default_type─┬─default_expression─┬─comment─┬─codec_expression─┬─ttl_expression─┐
│ title               │ String │              │                    │         │                  │                │
│ speaker_fname       │ String │              │                    │         │                  │                │
│ speaker_lname       │ String │              │                    │         │                  │                │
│ topic               │ String │              │                    │         │                  │                │
│ book                │ String │              │                    │         │                  │                │
│ chapter             │ Int32  │              │                    │         │                  │                │
│ s_verse             │ Int32  │              │                    │         │                  │                │
│ e_verse             │ Int32  │              │                    │         │                  │                │
│ dt                  │ Date   │              │                    │         │                  │                │
│ part_num            │ Int32  │              │                    │         │                  │                │
│ file_type           │ String │              │                    │         │                  │                │
│ file_location       │ String │              │                    │         │                  │                │
│ url_location        │ String │              │                    │         │                  │                │
│ notes_url           │ String │              │                    │         │                  │                │
│ notes_file_location │ String │              │                    │         │                  │                │
└─────────────────────┴────────┴──────────────┴────────────────────┴─────────┴──────────────────┴────────────────┘

15 rows in set. Elapsed: 0.023 sec. 

80242fc290bc :) 

```