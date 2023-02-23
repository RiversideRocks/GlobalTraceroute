import requests
import os
from dotenv import load_dotenv

load_dotenv()

def ping():
    requests.post(os.getenv("BACKEND") + "/api/v1/ping", data={"machineID": os.getenv("MACHINE_ID")}, headers={"User-agent": "Global Traceroute " + os.getenv("VERSION")})

def getMachineID():
    return os.getenv("MACHINE_ID")