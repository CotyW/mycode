import requests

baseurl = ""
sign = input("")
url = baseurl + sign

print(url)

response = requests.get(url)
#get, post, put, delete

response = response.json()

print(response)


