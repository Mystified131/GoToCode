import requests

print("")

link = input("Please enter the URL from which you would like to gather text, without the the http:// prefix: ")

print("")

ur = "http://" + link

f = requests.get(ur)
print(f.text)