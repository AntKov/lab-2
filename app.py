from flask import Flask, request
from datetime import date
# import  datetime 

app =  Flask(__name__)

@app.route("/")

def hellow_world():

 toSaturday=6-int(date.today().strftime('%w'))
 today=date.today().strftime('%A')
 if  toSaturday==0:
  return f"<p> Today is Saturday </p>   "
 else: 
  return f" <p> Today is {today} </p>     <p> {toSaturday}  day(s) left until the nearest Saturday</p>"
