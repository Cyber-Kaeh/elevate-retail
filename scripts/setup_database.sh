#!/bin/bash

# Configuration
SQL_SERVER_IMAGE="mcr.microsoft.com/mssql/server:2019-latest"
CONTAINER_NAME="sqlserver"
SA_PASSWORD="Secure1passw0rd"
DATABASE_NAME="elevate_retail"
SQL_SCRIPTS_PATH="/tmp"
CREATE_TABLE_SCRIPT="${SQL_SCRIPTS_PATH}/Elevate_Create_Table.sql"
INSERT_DATA_SCRIPT="${SQL_SCRIPTS_PATH}/Elevate_Insert.sql"

# Function to run a command and handle errors
run_command() {
    echo "Running: $*"
    "$@"
    if [ $? -ne 0 ]; then
        echo "Error: Command failed: $*"
        exit 1
    fi
}

# Pull the SQL Server Docker image
echo "Pulling SQL Server Docker image..."
run_command docker pull "$SQL_SERVER_IMAGE"

# Start the SQL Server container
echo "Starting SQL Server container..."
run_command docker run -d \
    --name "$CONTAINER_NAME" \
    -e "ACCEPT_EULA=Y" \
    -e "MSSQL_SA_PASSWORD=$SA_PASSWORD" \
    -p 1433:1433 \
    "$SQL_SERVER_IMAGE"

# Wait for SQL Server to be ready
echo "Waiting for SQL Server to be ready..."
for i in {1..10}; do
    docker exec "$CONTAINER_NAME" /opt/mssql-tools18/bin/sqlcmd \
        -S localhost -U SA -P "$SA_PASSWORD" -C -Q "SELECT 1" &> /dev/null
    if [ $? -eq 0 ]; then
        echo "SQL Server is ready!"
        break
    fi
    echo "SQL Server is not ready yet. Retrying in 5 seconds..."
    sleep 5
done

# Exit if SQL Server is not ready after retries
if [ $? -ne 0 ]; then
    echo "SQL Server did not become ready in time. Exiting."
    exit 1
fi

# Create the database
echo "Creating database '$DATABASE_NAME'..."
run_command docker exec "$CONTAINER_NAME" /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P "$SA_PASSWORD" -C -Q "CREATE DATABASE $DATABASE_NAME;"

# Copy sql files into container
docker cp ~/elevate-retail/src/config/Elevate_Create_Table.sql sqlserver:/tmp
docker cp ~/elevate-retail/src/config/Elevate_Insert.sql sqlserver:/tmp
echo "SQL files successfully copied into container"

# Run the SQL scripts
echo "Creating tables..."
run_command docker exec -i "$CONTAINER_NAME" /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P "$SA_PASSWORD" -d "$DATABASE_NAME" -C -i "$CREATE_TABLE_SCRIPT"

echo "Inserting data into tables..."
run_command docker exec -i "$CONTAINER_NAME" /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P "$SA_PASSWORD" -d "$DATABASE_NAME" -C -i "$INSERT_DATA_SCRIPT"

echo "Database setup completed successfully!"
