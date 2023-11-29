from datetime import datetime

import requests

USER_NAME = "huibaekim"
TOKEN = "asd!@as0zxclkkasdk12k4!@$@12asll3$%@!#$"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#response.raise_for_status()

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config ={
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers={
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#response.raise_for_status()

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20.0",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
response.raise_for_status()