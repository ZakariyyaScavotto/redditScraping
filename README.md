# redditScraping

This is a project I've started this summer (2022) about webscraping by experimenting with gathering information from Reddit.

The goal is to in the end create a minature demonstration Python application that allows for someone to do a search on Reddit and be able to look at the memes that match that search.

## Running the program

To run this program, certain Python libraries need to be installed:

- praw (Library to interact with Reddit and get information/images)
- opencv-python aka cv2 (Library to manipulate images)
- imutils (Library to manipulate images)
- pillow aka PIL (Library to manipulate images)
- python-dotenv aka dotenv (Library to interact with .env file)

Once these libraries are installed, you will need to create an application on Reddit [https://ssl.reddit.com/prefs/apps/]. For help with doing this, I would recommend looking at this article that walks through the process [https://towardsdatascience.com/scraping-reddit-data-1c0af3040768].

Now that these are setup, all that's left is to create a .env file in the same folder as the program with your given client_id, client_secret, and user_agent. A template .env file has been added with the repo. With these things all done, you should be ready to run the program.

### DISCLAIMER

This program is not meant to be a replacement for browsing Reddit in any way. It is intended to and created to be used for purely educational purposes. If you want to look at memes and upvote them, actually use Reddit.
