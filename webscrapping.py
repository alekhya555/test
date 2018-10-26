import requests
from bs4 import BeautifulSoup
search="foss@amrita"
url="http://www.google.co.in/search?q=" + search
response=requests.get(url)
soup=BeautifulSoup(response.text, "lxml")
for i in soup.select(" .r a"):
  print(i.text)
