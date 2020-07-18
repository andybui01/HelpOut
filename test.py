from flask import Flask, render_template, request, redirect, url_for, abort, session
import requests
import argparse

app = Flask(__name__)

@app.route("/")
def start():
	return redirect(url_for('home'))

@app.route("/home", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		if request.form["button"] == "start":
			return redirect(url_for('user'))
	else:
		return render_template('home.html')

@app.route("/volunteer", methods=["GET", "POST"])
def volunteer():
	if request.method == "POST":
		if request.form["button"] == "start":
			return redirect(url_for('user'))
	else:
		return render_template('volunteer.html')

@app.route("/about_us", methods=["GET", "POST"])
def camera():
    
    if request.method == "POST":
        if request.form["button"] == "back":
            return redirect(url_for('user'))
    else:
        return render_template('about_us.html')
    
if __name__ == '__main__':
        app.run(debug=True, port = 8000)