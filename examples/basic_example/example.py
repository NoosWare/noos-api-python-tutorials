import requests
from os import getcwd

# Read the logins for the platform
logins = open(".noos_credentials").read().splitlines();
headers = {
    'User-Token': logins[0], # username
    'Accept-Token': logins[1] # password
};

# The form to submit
file_path = getcwd() + '/../data/face.jpg'
files = {
    'filename': (file_path, open(file_path, 'rb'))
}

url = 'https://demo.noos.cloud:9001/face_detection'
response = requests.post(url, headers=headers, files=files)

print(response.json())