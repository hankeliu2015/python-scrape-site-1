import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from decouple import config
import csv

# testing csv file

fields = ['User Name', 'Date | Time', 'Likes',
          'Comments', 'Numbers of Replies', 'Comment Sources']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "csv_file_test_1.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

##
# use environment variables for youtube api requests
YOUTUBE_API_SERVICE_NAME = config('YOUTUBE_API_SERVICE_NAME')
YOUTUBE_API_VERSION = config('YOUTUBE_API_VERSION')
DEVELOPER_KEY = config('DEVELOPER_KEY')

# targeted video for comments
# if "exceeding your quota error" shows up, try a different video id.
# video_id = "Oe421EPjeBE"
video_id = "QwZT7T-TXT0"

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)


# create a Youtube api request to get all the comments on the video
request = youtube_object.commentThreads().list(
    part="id, snippet",
    order="time",
    textFormat="html",
    videoId=video_id)
# video_comments = request.execute()
# print(video_comments)
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
