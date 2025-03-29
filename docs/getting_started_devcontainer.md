# Getting Started with Dev Containers

This is probably the most difficult of the 3 options because it is the most involved, takes the most time, and therefore has the most potential for something to go wrong.  

Still, I highly recommend learning this and using these technologies. Keeping everything in a container (kind of like a small virtual machine) keeps everything in one place and gives you complete control over what goes on inside that container. You don't have to worry about changing anything on your local machine, such as language versions, packages, distributions, OSes... Everything you need to write a program can be pre-set in the Dev Container then destroyed when finished, keeping it off your machine while maintaining compatibility with other machines.  

## Prerequisites

- **Hardware**
    - Minimum CPU with 4 cores and 8 GB RAM
    - Virtualization enabled in BIOS might be necessary for Docker

- **Operating System**
    - 64 bit OS.
    - If you are on a modern Windows or Mac your fine
    - If you are using Linux this... guide probably isn't for you, you're fine.

- **Software**
    - **Windows & Mac**
        - Docker Desktop
        - VS Code
    - **Linux**
        - Docker Engine (plenty of great guides online)

- **Services**
    - GitHub account.

## Install Docker

This really isn't difficult. There are plenty of guides and tutorials to help if you run into any problems. One common problem I've heard of is that some Windows machines need virtualization enabled in BIOS. Search for that on Google if needed. If you are using Windows Pro, you should be fine.

Follow the instructions on the official website for your OS.  
[Get started with Docker](https://docs.docker.com/get-started/)

Once you have it installed and running, try pulling an image to make sure everything is working. There is a `hello-world` image they recommend for this.

## Install VS Code

If you don't already have Visual Studio Code installed, head over to their website and follow along. I highly recommend it anyway, but it is required for this setup.

[Download VS Code](https://code.visualstudio.com/download)

In VS Code, install these extensions:
- Pylance (Microsoft)
- Dev Containers (Microsoft)
- Docker (Microsoft)

## Set up a New Dev Container

1. Clone the projects repository
    - Open a command line. Windows: Command Prompt, PowerShell. Mac/Linux: Terminal. Terminal in VS Code.
    * Make sure you are in the directory where you want the project files!
    - `git clone https://github.com/Cyber-Kaeh/elevate-retail`
    - `cd elevate-retail`
2. Open the project in VS Code
    - `code .`
    - Or use File > Open Folder
3. Open the Command Pallet in VS Code
    - `Ctrl+Shift+P` Windows
    - `Cmd+Shift+P` Mac
4. Search for and select:
    - **Dev Containers: Reopen in Container**

5. Follow the prompts.

There is a `.devcontainer` folder already in the project that will mostly tell VS Code what to do, but depending on your system and configuration, it may ask for additional information.  

I can't predict exactly what those questions will be, but the main thing to keep in mind is to stick with defaults. If/when asked about the container image, select the basic "Python 3" image.  

It is also important to note that it may automatically ask you if you want a Dev Container set up—click **Yes** if prompted. More importantly, be patient. On the first run, this could take quite a while depending on your system and internet connection. If something goes wrong, scrap it and try again. That is another awesome feature of containers: they are basically disposable.  

If you get stuck:
- Check the docs or tutorials.
- Use message boards (StackOverflow, Reddit) or AI.
- IT trick #1: Restart your computer and try again.
- This is last, but it doesn't have to be a last resort! Reach out to me on Teams at any time!

## <u>Navigation</u>
- [Home](../README.md)
- [Next Steps](./starting_the_app.md)
- [Other Options](../README.md#getting-started)
- [Git Crashcourse](./git-crashcourse.md)