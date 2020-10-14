import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter URL - ")
data = urllib.request.urlopen(url).read()
info = json.loads(data)
count = 0
for i in range(len(info["comments"])):
    count = count + int(info["comments"][i]["count"])
print("sum:", count)
