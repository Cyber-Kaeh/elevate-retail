# elevate-retail
Forsyth Tech class of '25 Capstone Project

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- [Git](https://git-scm.com/)
- [Python 3.8+](https://www.python.org/downloads/)  <!-- Replace this with the specific version you are using -->
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
- [VS Code Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Getting Started

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository

Open a terminal and run the following command to clone the repository:

```bash
git clone https://github.com/Cyber-Kaeh/elevate-retail.git
cd elevate-retail
```

### 2. Set Up a Virtual Environment

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

### 3. Install Dependencies

Install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Open the Project in VS Code

Open VS Code and navigate to the project directory:

```bash
code .
```
  
## Using the Flask app
### Starting the web app
- Open a new terminal in VS Code
- Ensure you are in the root directory of the elevate retail project.
- Start the app with this flask command:  
  ```bash
  flask --app app run
  ```
- You should see output similiar to this:
```bash
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```
- Navigate to the address listed, or in VS Code `Ctl + click` on the link

### Shutting down
To stop the running flask app navigate back to the terminal in VS Code enter `Ctl + c`
This will stop the server and return your access to the terminal.

## Important Notes
- Do not push changes to main branch. Always (_always_) create a new branch for developing new features.
- If you want to run the app in 'debug' mode add the debug flag to the end of the command when starting the Flask app. Debug mode will allow you to make changes to the app and see them in real time, or with a reload, as apposed to having to shut down and restart the server.  
  ```bash
  flask --app app run --debug
  ```
- Flask is a lightweight but very powerful framework for Python. Using it is like using any other library we have learned about in class, like TKinter, NumPy, or Pandas. There is a learning curve for getting used to it, but it still just uses Python3 under the hood and solves problems the same way. We still have to think through the problems and figure out how to solve them with Python. Flask will just help us by reducing the lines of code we actually have to type, but the trade-off is we will have to scour the documentation and forums to figure out how to translate our solutions.
- This is more of a side note: I included Bootstrap v5.3 in this project to make the front-end stuff easier and faster. It is a framework for CSS and is pretty awesome, but we shouldn't have to worry about it too much.

# External Links

[Flask Documentation](https://flask.palletsprojects.com/en/stable/quickstart/)  
[Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
