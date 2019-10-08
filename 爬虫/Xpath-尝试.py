import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.sohu.com/a/225904132_609569")

soup = BeautifulSoup(request.text,'lxml')
p = soup.find(name='p',attrs={'data-role':"original-title",'style':"display:none"})
print(p)
