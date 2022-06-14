'''
Helpful articles
https://blog.devgenius.io/scraping-reddit-with-praw-python-reddit-api-wrapper-eaa7d788d7b9
praw.readthedocs.io/en/stable 
https://www.reddit.com/wiki/search
'''

import praw, re

from dotenv import load_dotenv
load_dotenv()
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), user_agent=os.getenv('USER_AGENT'))

query = 'Kenobi'
sub = 'PrequelMemes'
sort = 'hot'
limit = 10

hotPosts = reddit.subreddit(sub).search(query, sort=sort, limit=limit)
# print(hotPosts) generic praw.modles ListingGenerator object

imagePattern = r'https:\/\/i.redd.it(.)+(\.jpg|\.png)'
allImagePosts = list()
for post in hotPosts:
    # print(vars(post))
    # image vars: 'preview', 'url' < THIS IS THE ONE
    if re.match(imagePattern, post.url):
        allImagePosts.append(post.url)

print('Done')