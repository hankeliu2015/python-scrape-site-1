import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from decouple import config

YOUTUBE_API_SERVICE_NAME = config('YOUTUBE_API_SERVICE_NAME')
YOUTUBE_API_VERSION = config('YOUTUBE_API_VERSION')
DEVELOPER_KEY = config('DEVELOPER_KEY')
video_id = "QwZT7T-TXT0"
# if recevie exceeding your quota error try a different video id.
# video_id = "Oe421EPjeBE"

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)


# create a request to get all the comments on the video
request = youtube_object.commentThreads().list(
    part="id, snippet",
    order="time",
    textFormat="html",
    videoId=video_id)

video_comments = request.execute()
print(video_comments)

# with open('video_comments-2.txt', mode='w') as file_object:
#     print(video_comments-2, file=file_object)

# user requests to fetch uri resource
# req = requests.get('https://www.geeksforgeeks.org')
# req = requests.get('https://www.youtube.com/watch?v=QwZT7T-TXT0')

# soup = BeautifulSoup(req.content, "html.parser")
# soup = BeautifulSoup(req.content, "lxml")
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
