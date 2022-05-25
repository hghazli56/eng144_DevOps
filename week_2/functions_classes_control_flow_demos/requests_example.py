import requests

request_bbc = requests.get("https://bbc.co.uk/")

print(request_bbc.content)