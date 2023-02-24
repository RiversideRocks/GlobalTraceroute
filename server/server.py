from flask import Flask, Response, request
import mysql.connector
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)
load_dotenv()

mydb = mysql.connector.connect(
  host=os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  password=os.getenv("PASSWORD"),
  database="traceroute"
)

@app.route('/')
def home():
    return Response("Hello!", content_type="text/plain")

@app.route('/hosts')
def home():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM traceroute")

    myresult = mycursor.fetchall()
    l = []
    for x in myresult:
        l.append(x)

    return Response(json.dumps(l), content_type="application/json")

if __name__ == '__main__':
    app.run(debug=True)