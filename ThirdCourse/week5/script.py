import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count = len(results)
s = 0
for result in results:
    s = s + int(result.find('count').text)
print(count)
print(s)
