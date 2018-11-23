import requests

resp = requests.get("http://backend:8090/poulet")
if resp.status_code != 200:
    raise Exception("GET /poulet {}".format(resp.status_code))
print(resp.json())

resp = requests.post("http://backend:8090/poulet", json={'type': 'braise'})
if resp.status_code != 200:
    raise Exception("POST /poulet {}".format(resp.status_code))
print(resp.json())
