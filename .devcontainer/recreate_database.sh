#!/bin/bash

# This script will recreate the database if the
# Elevate_Create_Table.sql and
# Elevate_Insert.sql files are modified.

# Configuration
SQL_SERVER_IMAGE="mcr.microsoft.com/mssql/server:2019-latest"
CONTAINER_NAME="sqlserver"
SA_PASSWORD="Secure1passw0rd"
DATABASE_NAME="elevate_retail"
SQL_SCRIPTS_PATH="/tmp"
CREATE_TABLE_SCRIPT="${SQL_SCRIPTS_PATH}/Elevate_Create_Table.sql"
INSERT_DATA_SCRIPT="${SQL_SCRIPTS_PATH}/Elevate_Insert.sql"

# Copy sql files into container
echo "Copying SQL files into container..."
docker cp /workspaces/elevate-retail/src/config/Elevate_Create_Table.sql sqlserver:/tmp
docker cp /workspaces/elevate-retail/src/config/Elevate_Insert.sql sqlserver:/tmp

# Run create table script
echo "Running $CREATE_TABLE_SCRIPT..."
docker exec -i "$CONTAINER_NAME" /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P "$SA_PASSWORD" -d "$DATABASE_NAME" -C -i "$CREATE_TABLE_SCRIPT"

# Run insert data script
echo "Running $INSERT_DATA_SCRIPT..."
docker exec -i "$CONTAINER_NAME" /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P "$SA_PASSWORD" -d "$DATABASE_NAME" -C -i "$INSERT_DATA_SCRIPT"
