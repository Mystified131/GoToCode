import requests

link = "https://www.krack.com/en/tech-info/Pages/default.aspx"
f = requests.get(link)
print(f.text)