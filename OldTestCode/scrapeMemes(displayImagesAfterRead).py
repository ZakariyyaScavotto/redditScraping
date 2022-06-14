'''
Helpful articles

'''
# NEED TO MAKE IMAGE VIEWER
import praw, re, requests, os
import tkinter as tk

from dotenv import load_dotenv
load_dotenv()
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), user_agent=os.getenv('USER_AGENT'))

def getImages():
    query = queryInput.get(1.0, "end-1c")
    if query == '': query='Kenobi'
    sub = subInput.get(1.0, "end-1c")
    if sub == '': sub = 'PrequelMemes'
    sort =  sortInput.get(1.0, "end-1c")
    if sort == '': sort='hot'
    limitText = limitInput.get(1.0, "end-1c")
    if limitText != '':
        limit = abs(int(limitText))
    else:
        limit = 50 #default

    hotPosts = reddit.subreddit(sub).search(query, sort=sort, limit=limit)
    imagePattern = r'https:\/\/i.redd.it(.)+(\.jpg|\.png)'
    allImagePosts = list()
    for post in hotPosts:
        if re.match(imagePattern, post.url):
            allImagePosts.append(post.url)
    # print('finished finding images')
    if not os.path.exists('images/'):
        os.makedirs('images')
    for imageURL in allImagePosts:
        tempURL = imageURL[8:-5].replace('/','.')
        data = requests.get(imageURL).content
        fullFileName = 'images/'+tempURL+'.jpg'
        if not os.path.exists(fullFileName):
            with open(fullFileName, 'wb') as handler:
                handler.write(data)
    # print('finished saving images')
    label.config(text='Finished')

frame = tk.Tk()
frame.title('Reddit Scraper')
frame.geometry('495x110')
frame.minsize(495, 110)
frame.resizable(width=True, height=False)

queryLabel= tk.StringVar()
queryLabel.set('Enter Search Term (ex: Kenobi)')
queryDir = tk.Label(frame, textvariable=queryLabel)
queryDir.grid(row=0,column=0, sticky=tk.W+tk.E+tk.N+tk.S)
queryInput = tk.Text(frame, height=1)
queryInput.insert(tk.END, "")
queryInput.grid(row=0,column=1, sticky='nsew')
subLabel= tk.StringVar()
subLabel.set('Enter Subreddit to Search (ex: PrequelMemes)')
subDir = tk.Label(frame, textvariable=subLabel)
subDir.grid(row=1,column=0, sticky='nsew')
subInput = tk.Text(frame, height=1)
subInput.insert(tk.END, "")
subInput.grid(row=1,column=1, sticky='nsew')
sortLabel= tk.StringVar()
sortLabel.set('Enter Sort Method (ex: hot)') #hot, top, new
sortDir = tk.Label(frame, textvariable=sortLabel)
sortDir.grid(row=2,column=0, sticky=tk.W+tk.E+tk.N+tk.S)
sortInput = tk.Text(frame, height=1)
sortInput.insert(tk.END, "")
sortInput.grid(row=2,column=1, sticky='nsew')
limitLabel= tk.StringVar()
limitLabel.set('Enter number of posts to look at (ex: 50)') #hot, top, new
limittDir = tk.Label(frame, textvariable=limitLabel)
limittDir.grid(row=3,column=0, sticky=tk.W+tk.E+tk.N+tk.S)
limitInput = tk.Text(frame, height=1)
limitInput.insert(tk.END, "")
limitInput.grid(row=3,column=1, sticky='nsew')

b = tk.Button(frame, text="Search Reddit", command=getImages)
b.grid(row=4,column=0, sticky=tk.W+tk.E+tk.N+tk.S)
label= tk.Label(frame, text="", font=('Calibri 15'), justify=tk.LEFT)
label.grid(row=4,column=1, sticky=tk.W)

frame.mainloop()
print('Program done')