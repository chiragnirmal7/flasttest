from flask import Flask, render_template, request
import os
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)