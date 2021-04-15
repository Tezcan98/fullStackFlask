from flask import Flask, render_template
import models


app = Flask(__name__,static_url_path='', 
            static_folder='static')

@app.route("/") 
@app.route("/index")
def home():
	return render_template("index.html")

@app.route("/create")
def create():
	return render_template("create.html")


if __name__ == "__main__":
	app.run()