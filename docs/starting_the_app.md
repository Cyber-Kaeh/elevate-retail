# Using the Flask App

## Starting the web App
- Open a new terminal in VS Code
- Ensure you are in the root directory of the elevate retail project.
- Start the app with this flask command:  
  ```bash
  flask --app app run
  ```
- You should see output similar to this:
```bash
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

## Viewing in a Web Browser
Once the app is started and you get the above message you can navigate to that address in a web browser to see a live view. In Codespaces or Dev Containers you will also get a pop up from VS Code asking if you want to view the webpage, you can click yes.

## Shutting Down
To stop the running flask app navigate back to the terminal in VS Code enter `Ctl + c`
This will stop the server and return your access to the terminal.

## Running in Debug Mode
If you want to make changes to the app and see them without having to restart the server every time then pass in the debug flag on initial flask command. I usually run in debug.
```bash
flask --app app run --debug
```

## Important Notes
- If the app runs but the browser window doesn't display more than a 'hello world' app then you may need to stop the app and make sure you're up to date with the repository. Check out the Git Crashcourse for more details on how to do that.
- Flask is a lightweight but very powerful framework for Python. Using it is like using any other library we have learned about in class, like TKinter, NumPy, or Pandas. There is a learning curve for getting used to it, but it still just uses Python3 under the hood and solves problems the same way. We still have to think through the problems and figure out how to solve them with Python. Flask will just help us by reducing the lines of code we actually have to type, but the trade-off is we will have to scour the documentation and forums to figure out how to translate our solutions.
- This is more of a side note: I included Bootstrap v5.3 in this project to make the front-end stuff easier and faster. It is a framework for CSS and is pretty awesome, but we shouldn't have to worry about it too much.

## <u>Navigation</u>
- [Home](../README.md)
- [Getting Started](../README.md#getting-started)
- [Git Crashcourse](./git-crashcourse.md)