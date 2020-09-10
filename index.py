#실시간 검색어가 두개씩 나옴 보완필요
#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://zum.com/#!/home')
soup = BeautifulSoup(response, 'html.parser')

f = open("새파일.txt", 'w')
i = 1
for anchor in soup.select("span.keyword.d_keyword"):
    data =str(i)+": "+ anchor.get_text()+"\n"
    i= i+1
    f.write(data)
f.close()
