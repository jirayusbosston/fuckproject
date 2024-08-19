import requests
import json
import time
from requests.auth import HTTPDigestAuth

robot_ip = '192.168.125.1'
rws = requests.Session()
rws.auth = HTTPDigestAuth("Default User", "robotics")
rwr=rws.get('http://'+robot_ip+'/rw?json=1')

def get_robot_data():
    # Construct the appropriate URL based on your robot's API
    url = 'http://' + robot_ip + '/rw/device/'
    response = rws.get(url)
    data = response.json()
    # Extract relevant data from the JSON response
    position = data.get('position', 0)
    speed = data.get('speed', 0)
    # ... other data points
    return {'position': position, 'speed': speed}

# Main logic to call get_robot_data and process/display the results
if __name__ == "__main__":
    while True:
        data = get_robot_data()
        # Process and display or store the data
        print(f"Position: {data['position']}, Speed: {data['speed']}")  # Replace with your desired output
        time.sleep(1)  # Adjust the sleep time as needed