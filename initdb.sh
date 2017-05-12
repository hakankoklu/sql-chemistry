#!/usr/bin/env bash

psql -c "drop database if exists literator_db;"
psql -c "drop user if exists some_user;"
createdb literator_db
psql -c "create user some_user; grant all privileges on database "literator_db" to some_user"
python populate_tables.py