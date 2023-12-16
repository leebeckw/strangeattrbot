import matplotlib.pyplot as plt
import os
import attractor
from dotenv import load_dotenv
import requests

load_dotenv()

# api keys
PAT = os.getenv("PERSONAL_ACCESS_TOKEN")

response = requests.post('https://api.are.na/v2/channels/strange-attractors-ceel2vxiqn0/blocks/', \
                  data={'source': 'https://media.githubusercontent.com/media/leebeckw/strangeattrbot/main/image.png'}, \
                    headers={'Authorization': 'Bearer ' + PAT, 'Cache-Control': 'no-cache'})


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the content of the response (e.g., JSON response)
    print(response.json())
else:
    # Print an error message if the request was not successful
    print("Error: {response.status_code}")
