from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('front_page.html')