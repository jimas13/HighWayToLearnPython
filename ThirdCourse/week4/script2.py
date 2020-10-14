from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
usercount = int(input('Enter count: '))
userposition = int(input('Enter position: '))
for i in range(usercount):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1

        #make it stop at position 3#
        if count>userposition:
            break
        url = tag.get('href', None)

print(url)
