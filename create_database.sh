#!/bin/bash
set -x

echo "CREATE DATABASE IF NOT EXISTS hoyj ENGINE = Memory COMMENT 'hoyj media search engine';" | clickhouse-client -mn

