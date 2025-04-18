# Getting Started with Codespaces

GitHub Codespaces is a cloud IDE solution to help teams work on a project in an
isolated development environment without having to worry about managing concerns
for operating systems and dependencies.  
Put simply, this allows us to use VS Code in a web browser with no local setup
or changes required.  
[Codespaces Documentation](https://docs.github.com/en/codespaces)

## Prerequisites

- A GitHub account
  
## Setup

1. Log in to GitHub and navigate to the repository:
    - https://github.com/Cyber-Kaeh/elevate-retail

2. Click on the 
<a href="#" 
   style="display: inline-block; 
          padding: 8px 16px; 
          font-size: 16px; 
          font-weight: bold; 
          color: #fff; 
          background-color: #2ea44f; 
          border-radius: 6px; 
          text-decoration: none;">
   <span> < > Code &#9660; </span>
</a>
 button and then 'Open with Codespaces'

3. Follow the on-screen instructions to set up your Codespaces environment
    - It should recognize that there is a .devcontainer file already present and ask if you want to use that, click yes.  
  
## Working with Codespaces

It may take some time for the environment to fully load and set up on the first run, perhaps several minutes depending on internet connection. When you have access to your terminal at the bottom and don't see anything else loading you are ready to start coding!

Example terminal prompt when ready:
```bash
vscode ➜ /workspaces/ft_capstone/elevate-retail (main) $
```

## Next Steps

*Submodules* have been initialized in this repository, thanks to the dedicated efforts
of Dallas (GitHub: nveeee).  

To be sure the module is intialized and new dependencies are updated the following
two commands must be run:

```bash
git submodule update --init --recursive
pip install -r requirements.txt
```

The .devcontainer file *should* also perform a `git pull` to ensure you are up to date with the current repository. If you don't see all the same files from the repository on the left or if you cannot start the Flask app, then it most likely did not automatically pull.  

That is ok though, because it is best practice to always make sure you are up to date every time you first sit down to code. I have outlined a brief Git crash course with the commands you should run the first time you start this project, along with every time you start a new coding session.  

Check out the crash course first, then head over to the instructions on how to start the project's web app.  

## Troubleshooting

**If you get stuck while the Codespaces is loading:**
- First be patient, it is a slow process. It can take up to 10 minutes.
- Second, it could be a configuration issue in my devcontainer.json
  - I'm looking into fixing this!

If you don't see "Would you like to install SQL Server 2019?" with a prompt to answer
yes/no, then something went wrong. Follow these steps as a temporary work around
until I can address the automation issue.

1. Close the terminal that is stuck on the spinning tab
2. Open a new terminal
3. IF this is a new Codespace:
  - We will need to **manualy run** the setup_database script:
  ```bash
    cd .devcontainer/
    chmod +x setup_database.sh  # make the script executable
    ./setup_database.sh  # run the script
  ```
  - You should now be prompted asking if you want to install SQL Server, select y
  - Important post install!
  `cd ..`
  - This puts you back in the root of the directory. Flask command will *not* work if
  you are still in the .devcontainer folder!

  *If this is an existing Codespace that had SQL Server working before:*
  ```bash
    docker start sqlserver  # Start it back up
    docker ps  # Check that the instance is running
  ```

**If you are having module errors or import errors**  

The submodules might not be loaded properly, try this command:
```bash
git submodule update --init --recursive
```
  

## <u>Navigation</u>
- [Home](../README.md)
- [Starting The App](./starting_the_app.md)
- [Other Options](../README.md#getting-started)
- [Git Crashcourse](./git-crashcourse.md)
