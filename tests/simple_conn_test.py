import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=127.0.0.1,1433;"
    "UID=SA;"
    "PWD=Secure1passw0rd;"
    "DATABASE=tempdb;"
    "TrustServerCertificate=yes;"
)

try:
    connection = pyodbc.connect(connection_string)
    cur = connection.cursor()
    cur.execute("SELECT @@version;")
    print("Connection successful!")
    connection.close()
except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    if sqlstate == '08001':
        print("Connection failed: Invalid connection string.")
    elif sqlstate == '28000':
        print("Connection failed: Invalid username or password.")
    elif sqlstate == '01000':
        print("Connection failed: General error.")
    else:
        print(f"Connection failed: {ex}")
finally:
    print(connection_string)
