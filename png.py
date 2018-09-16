url='http://pngimg.com/uploads/viber/viber_PNG25.png'
import urllib
urllib.urlretrieve(url, "test.png")
import requests
r=requests.get(url)
with open("test.png", "wb")as code:
	code.write(r.content)
n=int(raw_input())
m=int(raw_input())
a=str(raw_input())
if(a=="+"):
	print(n+m)
elif(a=="-"):
	print(n-m)
elif(a=="*"):
	print(n*m)
else:
	print(n/m)
