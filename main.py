#using fixer.io api to get rates and prices

import requests
import json

from config import url

def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    with open("archive/"+filename+".json", 'w') as f:
        f.write(json.dumps(rates))


if __name__ == '__main__':
    response = get_rates()
    archive(str(response['timestamp']), response['rates'])




