#  from https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
import praw

from dotenv import load_dotenv
load_dotenv()
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), user_agent=os.getenv('USER_AGENT'))

# get 10 hot posts from the MachineLearning subreddit
hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
for post in hot_posts:
    print(post.title)

# get hottest posts from all subreddits
hot_posts = reddit.subreddit('all').hot(limit=10)
for post in hot_posts:
    print(post.title)

# put data into a dataframe
import pandas as pd
posts = []
ml_subreddit = reddit.subreddit('MachineLearning')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)

# get MachineLearning subreddit data
ml_subreddit = reddit.subreddit('MachineLearning')

print(ml_subreddit.description)


# specific post
submission = reddit.submission(url="https://www.reddit.com/r/MapPorn/comments/a3p0uq/an_image_of_gps_tracking_of_multiple_wolves_in/")
# or 
submission = reddit.submission(id="a3p0uq")

# get top-level comments, breaks because of MoreComments
# for top_level_comment in submission.comments:
    # print(top_level_comment.body)

# check data type of each comment before printing body
from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)

# replace morecommments
submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)

# get all comments in comment section, printing by level (1st level, 2nd level, etc.)
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    print(comment.body)