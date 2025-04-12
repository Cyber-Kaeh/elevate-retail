# Working with SQL Server inside the project

When running this project in a dev container you will be prompted at the
end if you want to install and set up SQL Server 2019. You may choose
yes or no and don't worry you can set it up later.  

This is the official Microsoft SQL Server container for Docker referenced
[here](https://hub.docker.com/r/microsoft/mssql-server).  

Included in the .devcontainer folder of this repository is a script, setup_database.sh,
that will automate pulling the container and setting up the database based
on the database scripts provided by the database team.  
..whew.. that was an extraneous use of the word database..

## Prerequisites

- Be working inside a dev container or codespace
- If attempting this locally Docker **must** be installed  

## How do I know it worked?

If you didn't get any catastrophic looking errors or massive amounts of red letters
you should be good to go. Run the following command in the terminal to perform a
simple query and see if it produces any results:

```bash
docker exec -i sqlserver /opt/mssql-tools18/bin/sqlcmd -S localhost -U SA -P Secure1passw0rd -d elevate_retail -C -Q "SELECT * FROM Inventory"
```

If that command returned these results you're all set!

```
Inventory_ID Product_ID  Quantity    Unit_Price Deleted_At                            
------------ ----------- ----------- ---------- --------------------------------------
           1           1        3000       6.99                                   NULL
           2           2         100     249.00                                   NULL
```

*The actual results will change as the database changes but the output should be similar*

## Breaking down the command

The above command is quite long so lets briefly break down what is going on with it.  

`docker exec -i`
This first portion of the command is just telling Docker that we want to execute a
command interactively inside a running container.  

`docker exec -i <container_name>`
The second part is specificing which container to execute the command. In this case
the name of the container is `sqlserver`.  

`docker exec -i sqlserver <where inside the container>`
Next up looks like it is getting a little hairy. Don't worry too much about this part,
it is basically just telling docker a file path to follow *inside* the container to
execute the command. In this case it's a path to the mssql tools directory with the
sqlcmd command in it. Again, hairy, lets keep it moving..

`docker exec -i sqlserver /opt/mssql-tools18/bin/sqlcmd <more flags than the U.N.>`
Now we know we want docker to execute something, and we're telling it where to do it we
have to set some flags (anything following a '-' usually). This is basically us
manually setting the connection string for accessing the database being hosted inside
SQL Server.
- -S --server
- -U --user name
- -P --password
- -d --database name
- -C --trust certificate
- -Q --query

Now is a good time to review the script and how it handles all of these
parameters. The most important thing to note is that most of these are
user defined in the `docker run` command. I only point this out because the values
passed in with these flags will **not** reflect the actually connection string used
to access the real Elevate Retail Database. This is just for this little test
environment. Also, don't forget the `-C`! SQL Server enforces certificates by default
so we must tell it to ignore their validity every time.  

Moving on...  

The entire command again, this time note the query is different. This is where you
can alter the command to query different tables or get information about the database.
```bash
docker exec -i sqlserver /opt/mssql-tools18/bin/sqlcmd -S localhost -U SA -P Secure1passw0rd -d elevate_retail -C -Q "SELECT * FROM Customer"
```

## Next Steps

This is just to get the Docker container with SQL Server up and running so we can
test things like connection strings and queries programatically.  

From here we can have a local, safe sandbox to experiment and break things without taking
up server time in the pods or interfering with the database team's
efforts to maintain the production database. If something does break in *this* database
then so what? Delete it and run the script again.  

## Final Notes

If you do want to clear out the existing container and start over follow these steps:  

1. Stop the container
    - `docker stop sqlserver`
2. Delete the container
    - `docker rm sqlserver`
3. Run the setup script again
    - `/scripts/setup_database.sh`

You should now have a fresh container restored to how it is defined in the .sql scripts from the database team.  

**Updating the .sql scripts**

Currently the scripts provided reside in the config folder of the project.
```
/src/config/Elevate_Create_Table.sql
/src/config/Elevate_Insert.sql
```


As long as the names stay exactly the same these files can be replaced with the newer
versions as they become available. If the name or location changes this could break
the setup script.  

## <u>Navigation</u>
- [Home](../README.md)
- [Getting Started](../README.md#getting-started)
- [Starting The App](./starting_the_app.md)
- [Git Crashcourse](./git-crashcourse.md)