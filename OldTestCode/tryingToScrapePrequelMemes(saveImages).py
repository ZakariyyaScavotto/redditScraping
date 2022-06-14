'''
Helpful articles
https://www.scrapingbee.com/blog/download-image-python/
https://stackoverflow.com/questions/30229231/python-save-image-from-url
'''

import praw, re, requests, os

from dotenv import load_dotenv
load_dotenv()
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), user_agent=os.getenv('USER_AGENT'))

query = 'Kenobi'
sub = 'PrequelMemes'
sort = 'hot'
limit = 50
hotPosts = reddit.subreddit(sub).search(query, sort=sort, limit=limit)

imagePattern = r'https:\/\/i.redd.it(.)+(\.jpg|\.png)'
allImagePosts = list()
for post in hotPosts:
    if re.match(imagePattern, post.url):
        allImagePosts.append(post.url)

if not os.path.exists('images/'):
    os.makedirs('images')
for imageURL in allImagePosts:
    tempURL = imageURL[8:-5].replace('/','.')
    data = requests.get(imageURL).content
    fullFileName = 'images/'+tempURL+'.jpg'
    if not os.path.exists(fullFileName):
        with open(fullFileName, 'wb') as handler:
            handler.write(data)

print('Done')