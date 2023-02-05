import os

import requests
import dotenv
import json
import os


def pinToIPFS(filename):
    dotenv.load_dotenv()

    url = "https://api.nft.storage/upload"
    headers = {
        "Content-Type": "*/*",
        "accept":"application/json",
        "Authorization":f"Bearer {os.getenv('YOUR_STORAGE_API_KEY')}"
    }


    with open(f"{filename}", 'rb') as f:
        file = f.read()

    response = requests.request("POST",url,headers=headers,data=file)

    res = response.json()

    if os.path.exists(f"{filename}"):
      os.remove(f"{filename}")
    else:
      print("The file does not exist")

    print(res)

    return res
