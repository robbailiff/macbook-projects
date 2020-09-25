# Import a Flask webserver from the Flask module
from flask import Flask, render_template

# Create an instance of the Flask class named 'app' which represents the web application
# __name__ refers to the current file (main.py)
app = Flask(__name__)

# The decorator represents the default page of the app ("/") and executes the function 'home()'
@app.route("/")
def home():
	return render_template("home.html") # Uses the Flask method render_template to look for the named file in the templates folder

@app.route("/about")
def about():
	return render_template("about.html") 

# The decorator represents a new route which executes the function 'rob()'
@app.route("/rob")
def rob():
	return "Hello Rob!"

# When you run the script the name "__main__" is assigned to it by Python
# The if statement prevents any other scripts from running
if __name__ == "__main__":
	app.run(debug = True)	# debug=True allows any errors that appear to be shown on the webpage