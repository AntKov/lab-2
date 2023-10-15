from flask import flask, request
from datetime import date

app =  flask(__name__)

@app.route("/")

def hellow_world ():

return f"<p> Today is </p>"

