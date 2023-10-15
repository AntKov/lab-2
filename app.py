from flask import Flask, request
from datetime import date

app =  Flask(__name__)

@app.route("/")

def hellow_world():
  return f"<p> Today is {date.today().strtime('%d/%m/%Y')}</p>"

