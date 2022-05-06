import requests as re

r = re.get("http://localhost:8080/hello")
print(r.text)