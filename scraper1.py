import requests
from bs4 import BeautifulSoup

# req = requests.get('https://www.geeksforgeeks.org')
req = requests.get('https://www.youtube.com/watch?v=QwZT7T-TXT0')

# soup = BeautifulSoup(req.content, "html.parser")
soup = BeautifulSoup(req.content, "lxml")
# soup = BeautifulSoup(req.content, "html5lib")

# with open('page_output_html5lib.txt', mode='w') as file_object:
#     print(soup.prettify, file=file_object)

with open('page_output_lxml.txt', mode='w') as file_object:
    print(soup.prettify, file=file_object)

# print(soup.prettify)

# siteText = soup.get_text()
# print(siteText)

# res = soup.title
# print(res.prettify)
# print(res.get_text())
