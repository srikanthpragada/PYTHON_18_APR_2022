import requests

resp = requests.get("http://worldclockapi.com/api/json/utc/now")
#print(resp.status_code)
# print(resp.text)

now = resp.json()  # JSON to Dict
print(now['currentDateTime'])
