# from https://www.dishy.dev/articles/scraping-images-from-reddit/
# ^ doesn't work?
import praw, re, requests

from dotenv import load_dotenv
load_dotenv()
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), user_agent=os.getenv('USER_AGENT'))

# regex to check for image url
REGEX_TEST = r"((http|https)://i.imgur.com/.+?(jpg|png))"
p = re.compile(REGEX_TEST, re.IGNORECASE)

# Check if a link still is exists
def checkLinkActive(url):
    request = requests.head(url)
    if request.status_code == 200:
        return True
    else:
        return False

# Add a letter to an imgur url to make a small thumbnail
def getImgurThumbnail(url, size):
    startStr = url[:(len(url)-4)]
    endStr = url[len(url)-4:]
    return startStr + size + endStr

def getImages(url):
    submission = reddit.submission(url=url)
    # Tell API to return all comment in thread, results are
    # paginated by default
    submission.comments.replace_more(limit=None)

    # Create RegEx object for matching images
    REGEX_TEST = r"((http|https)://i.imgur.com/.+?(jpg|png))"
    p = re.compile(REGEX_TEST, re.IGNORECASE)

    imageMatches = []
    for comment in submission.comments.list():
        matches = p.findall(comment.body)
        for match in matches:
            if checkLinkActive(match[0]):
                imageMatches.append(
                    {"image": match[0], "thumbnail": getImgurThumbnail(match[0], "m")}
                )

    return imageMatches
