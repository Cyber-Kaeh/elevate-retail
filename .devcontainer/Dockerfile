FROM mcr.microsoft.com/devcontainers/python:3

# Install ODBC Driver and pyodbc
RUN apt-get update && apt-get install -y curl gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    pip install pyodbc
    
# Expose port 1433 for SQL Server
EXPOSE 1433

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy and make the setup_database.sh script executable
COPY setup_database.sh /scripts/setup_database.sh
RUN chmod +x /scripts/setup_database.sh
