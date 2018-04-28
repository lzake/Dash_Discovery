import urllib.request
url = input("Enter JSON URL: ")
with urllib.request.urlopen(url) as response:
   html = response.read()
print(html)