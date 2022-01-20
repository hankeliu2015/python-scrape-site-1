import requests
from bs4 import BeautifulSoup
from apiclient.discovery import build
from decouple import config

YOUTUBE_API_SERVICE_NAME = config('YOUTUBE_API_SERVICE_NAME')
YOUTUBE_API_VERSION = config('YOUTUBE_API_VERSION')
DEVELOPER_KEY = config('DEVELOPER_KEY')

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)

print(youtube_object)

# req = requests.get('https://www.geeksforgeeks.org')
req = requests.get('https://www.youtube.com/watch?v=QwZT7T-TXT0')

# soup = BeautifulSoup(req.content, "html.parser")
soup = BeautifulSoup(req.content, "lxml")
# soup = BeautifulSoup(req.content, "html5lib")

# with open('page_output_html5lib.txt', mode='w') as file_object:
#     print(soup.prettify, file=file_object)

# with open('page_output_lxml.txt', mode='w') as file_object:
#     print(soup.prettify, file=file_object)

# print(soup.prettify)

# siteText = soup.get_text()
# print(siteText)

# res = soup.title
# print(res.prettify)
# print(res.get_text())
