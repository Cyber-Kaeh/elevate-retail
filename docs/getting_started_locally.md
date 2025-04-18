# Getting Started Locally

:warning: This is no longer the suggested approach! :warning:  
Due to the dependency on SQL Server running in a Docker container I don't recomend cloning
locally because you will have to also have Docker set up and configure the networking to
connect to the sqlserver container.  

Follow these steps to set up and run the project on your local machine:

## 1. Clone the Repository

Open a terminal and run the following command to clone the repository:

```bash
git clone --recurse-submodules -j8 https://github.com/Cyber-Kaeh/elevate-retail.git
cd elevate-retail
```

## 2. Set Up a Virtual Environment

Create a virtual environment to manage your project dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

## 3. Install Dependencies

Install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 4. Run Git Fetch & Git Pull

Make sure the repository and branches are up to date by running these commands in the terminal:

```bash
git fetch --all
git pull origin main
```

## <u>Navigation</u>
- [Home](../README.md)
- [Next Steps](./starting_the_app.md)
- [Other Options](../README.md#getting-started)
- [Git Crashcourse](./git-crashcourse.md)