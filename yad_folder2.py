import json

import requests

with open('sens.txt') as f:
    file = json.loads(f.read())
    ya_token = file["token_ya"]


def yad_folder_creation(token):
    ya_api_base_url = "https://cloud-api.yandex.net"
    base_headers = {"Authorization": token}

    url = f'{ya_api_base_url}/v1/disk/resources'
    params = {"path": "lenses_scrap_dat1a"}
    response = requests.put(url, headers=base_headers, params=params)

    print(response.status_code)


if __name__ == "__main__":
    yad_folder_creation(ya_token)
