from flask import Flask, request
from datetime import date

app =  Flask(__name__)

@app.route("/")

def hellow_world():
 # todayDoW=7-date.today().strftime('%u')
#  return f"<p> Today is {date.today().strftime('%d/%m/%Y  %A')}</p>   "
#  <p> it is {todayDoW} till next Sunay </p> 
  return f"<p> date.today().strftime('%u')</p>   "
