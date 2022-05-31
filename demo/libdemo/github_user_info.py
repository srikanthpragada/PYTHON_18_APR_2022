import requests

userid = "gvanrossum123"

try:
    resp = requests.get(f"https://api.gitub.com/users/{userid}")
    if resp.status_code != 200:
        if resp.status_code == 404:
            print("Sorry! Invalid userid!")
        else:
            print("Sorry! Could not get details!")

        exit()
except:
    print("Sorry! Could not make request!")
    exit()

details = resp.json()  # JSON to Dict
print(details['name'])
print(details['public_repos'])
