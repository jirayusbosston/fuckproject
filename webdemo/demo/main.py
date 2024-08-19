import requests
import json
import time
from requests.auth import HTTPDigestAuth
from threading import Thread, Event

robot_ip = '192.168.125.1'
print('###########')
print('Start......')

# RWS Session Setup
rws = requests.Session()
rws.auth = HTTPDigestAuth("Default User", "robotics")
rws.headers = [('Content-Type', "application/x-www-form-urlencoded")]

def fetch_robot_data():
    position_endpoint = f'http://{robot_ip}/rw/motionsystem/mechunits/ROB_1/jointtarget/?json=1'
    energy_endpoint = f'http://{robot_ip}/rw/rapid/symbol/data/RAPID/T_ROB_L/MainModuleL/nEnergy?json=1'
    
    # Fetch Position
    r = rws.get(position_endpoint)
    position = r.json()['_embedded']['_state'][0]['value']
    print(f"Position: {position}")
    
    # Fetch Energy Usage
    r = rws.get(energy_endpoint)
    energy = r.json()['_embedded']['_state'][0]['value']
    print(f"Energy Usage: {energy}")

    # Add more fetches here as needed

def main():
    event = Event()
    t = Thread(target=fetch_robot_data, args=())
    t.start()
    
    while True:
        # Implement your main control loop here
        time.sleep(1)

if __name__ == "__main__":
    main()
