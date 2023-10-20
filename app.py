from flask import Flask, request
from datetime import date
# import  datetime 

app =  Flask(__name__)

@app.route("/")

def hellow_world():

  toSaturdat=7-int(date.today().strftime('%u'))

 
 if  toSaturdat==0:
   return f"<p> Today is Sunday </p>   "
 else: 
  return f"<p> {toSaturdat} </p>   "
