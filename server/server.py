from flask import Flask, Response, request
import mysql.connector
import os
from dotenv import load_dotenv
import json
import requests

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
def hosts():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM traceroute")

    myresult = mycursor.fetchall()
    l = []
    for x in myresult:
        l.append(x)

    return Response(json.dumps(l), content_type="application/json")

@app.route('/add', methods=["POST"])
def add():
    mycursor = mydb.cursor()
    try:
        ip = request.form["ip"]
        token = request.form["token"]
        if token != os.getenv("TOKEN"):
            return "Invalid token"
        
        api = requests.get("https://ipapi.co/" + str(ip) + "/json").json()
        city = api["city"]
        region = api["region"]
        country = api["country_name"]
        lat = str(api["latitude"])
        lon = str(api["longitude"])

        sql = "INSERT INTO traceroute (IP, City, Region, Country, Lat, Lon) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (ip, city, region, country, lat, lon)
        mycursor.execute(sql, val)
        return "OK"
    except:
        return "Missing IP/token param"

@app.route('/clear', methods=["POST"])
def clear():
    token = request.form["token"]
    if token != os.getenv("TOKEN"):
        return "Invalid token"
    mycursor = mydb.cursor()

    sql = "DELETE FROM traceroute WHERE 1=1"

    mycursor.execute(sql)

    mydb.commit()
    return "OK"


if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0)