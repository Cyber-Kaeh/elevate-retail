# elevate-retail
Forsyth Tech class of '25 Capstone Project

## Quick start guide
### To start the GitHub Codespace
- Click on the green button toward the upper right: [< > Code]
- Click on the link for the name of the Codespace: "shiny space spork"
  - I didn't choose the name but I dig it

After authenticating you should be directed to a new browser tab with an instance of VS Code running and the project already open.

### Starting the web app
*This will take place inside VS Code Codespace that opens*
- Ensure the terminal is running and ready to accept commands.
  - It may take a few minutes for the environment to completely load, you will see a typical command line when ready
- Ensure you are in the root directory of the elevate retail project.
- Start the app with this flask command:
  `flask --app app run`
- A pop up will annouce you may view the running application in a browser window.
  - This is good. Click it! If it fails ensure flask command is properly typed. If still fails contact support with error code.
- Enjoy! You should see the web page in another browser window now, if not retrace steps or contact support.

### Shutting down
To stop the running flask app navigate back to the terminal in VS Code enter [ctl + c]
This will stop the server and return your access to the terminal.
To stop the Codespace you can close out the browser window.

## Important Notes
- Do not push changes to main branch. Always (_always_) create a new branch for developing new features.
- The flask app is currently running in debug mode so that means you _should_ be able to make changes to the code and it will automatically update. Sometimes the changes don't take effect though, so just stop the server in the terminal with [ctl + c] then retstart with `flask --app app run`
- You can clone this repository to your local machine to work on it or test with it but you must make sure all versions and dependcies line up correctly. This Codespace will hopefully eliminate the "I dunno, it runs on my machine" problem... hopefully.
- Flask is a lightweight but very powerful framework for Python. Using it is like using any other library we have learned about in class, like TKinter, NumPy, or Pandas. There is a learning curve for getting used to it, but it still just uses Python3 under the hood and solves problems the same way. We still have to think through the problems and figure out how to solve them with Python. Flask will just help us by reducing the lines of code we actually have to type, but the trade-off is we will have to scour the documentation and forums to figure out how to translate our solutions.
- This is more of a side note: I included Bootstrap v5.3 in this project to make the front-end stuff easier and faster. It is a framework for CSS and is pretty awesome, but we shouldn't have to worry about it too much.

# External Links

[Flask Documentation](https://flask.palletsprojects.com/en/stable/quickstart/)  
[Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
