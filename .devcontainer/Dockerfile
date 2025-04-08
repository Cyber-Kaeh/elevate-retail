FROM mcr.microsoft.com/devcontainers/python:3

# Install ODBC Driver and pyodbc
RUN apt-get update && apt-get install -y curl gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    pip install pyodbc

# Set up a SQL Server container
RUN docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Secure1passw0rd" -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest

# Expose port 1433 for SQL Server
EXPOSE 1433

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt