from flask import Flask, request
from datetime import date
# import  datetime 

app =  Flask(__name__)

@app.route("/")

def hellow_world():

  todayDoW=7-int(date.today().strftime('%u'))
#  return f"<p> Today is {date.today().strftime('%d/%m/%Y  %A')}</p>   "
#  <p> it is {todayDoW} till next Sunay </p> 
  return f"<p> {todayDoW} </p>   "
