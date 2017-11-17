# Web Scraper using Beautiful Soup
# Created By - Javeed Basha H
# Completion Date - 11/11/2017
# Last Modified - 15/11/2017

# importing libraries
from requests import get
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import numpy as np
from time import sleep, time
from random import randint
from IPython.core.display import clear_output
from warnings import warn

print("##### Initiating Web Scraping Process #####")

# variables
posts = []
posted_by = []
comments = []
views = []
replies = []
post_date = []
last_replied = []

# initialising the time loop
start_time = time()
requests = 0

# page initialization - 5 pages
pages = [str(i) for i in range(1, 6)]

# code - beginning - data fetch
for page in pages:

    # GET response initialization
    response = get("web_page"+page)

    print("Scraping Web Page: ", page)

    # pausing the loop
    sleep(randint(8, 15))

    requests += 1
    elapsed_time = time() - start_time
    print('Request: {}; Frequency: {} requests/s'. format(requests, requests/elapsed_time))
    clear_output(wait=True)

    if response.status_code != 200:
        warn('Request: {}; Status Code: {]'.format(requests, response.status_code))

    # loop break if number of requests is greater than expected
    if requests > 72:
        warn('WARNING!!! - Requests limit has been exceeded.')
        break

    # regular parsing code - Beautiful Soup
    html_soup = bs(response.text, 'html.parser')

    # initialising the required container
    data_container = html_soup.find_all("li", class_="threadbit")

    # running loop - 2
    for data in data_container:

        # posts
        title = data.h3.a.text
        posts.append(title)

        # comments
        comm = data.find("div", class_="threadinfo", title=True)
        comments.append(comm['title'])

        # author name
        aut = data.find("a", class_="username understate").text
        posted_by.append(aut)

        # statistics
        statistics = data.find("ul", class_='threadstats td alt')
        # views
        view = re.findall(r"\bViews:\D*(\d[\d,]*)", str(statistics))
        views.append(view)
        # replies
        repl = re.findall(r"\bReplies:\D*(\d[\d,]*)", str(statistics))
        replies.append(repl)

        # posted date
        date_input = data.find("a", class_ = "username understate", title = True)
        # Using regex
        sample = date_input['title']
        match = re.findall(r'\d{2}-\d{2}-\d{4}', sample)
        post_date.append(match)

        # last post date
        date_output = data.div.find("dl", class_="threadlastpost td")
        match_1 = re.findall(r'\d{2}-\d{2}-\d{4}', str(date_output))
        last_replied.append(match_1)


print("##### Analyzing Outcome #####")
print("Length of title: ", len(posts))
print("Length of comments: ", len(comments))
print("Length of author names: ", len(posted_by))
print("Length of views: ", len(views))
print("Length of replies: ", len(replies))
print("Length of post date: ", len(post_date))
print("Length of last replied date: ", len(last_replied))

# dataframe conversion
pdi_thread = pd.DataFrame({
    "title": posts,
    "thread_comment": comments,
    "author": posted_by,
    "views": views,
    "replies": replies,
    "post_date": post_date,
    "last_replied_date": last_replied
})

# removing square brackets[]
pdi_thread['views'] = pdi_thread['views'].str[0]
pdi_thread['replies'] = pdi_thread['replies'].str[0]
pdi_thread['post_date'] = pdi_thread['post_date'].str[0]
pdi_thread['last_replied_date'] = pdi_thread['last_replied_date'].str[0]

# filling missing values
pdi_thread['last_replied_date'] = pdi_thread['last_replied_date'].fillna('11-16-2017')
pdi_thread['post_date'] = pdi_thread['post_date'].fillna('11-16-2017')

# type conversion
pdi_thread['post_date'] = pd.to_datetime(pdi_thread['post_date'])
pdi_thread['last_replied_date'] = pd.to_datetime(pdi_thread['last_replied_date'])
pdi_thread['replies'] = pdi_thread['replies'].astype(int)
pdi_thread['views'] = pdi_thread['views'].str.replace(",", "")
pdi_thread['views'] = pdi_thread['views'].astype(int)

# adding new column
pdi_thread['lifetime'] = pdi_thread['last_replied_date'] - pdi_thread['post_date']

# converting days in float64
pdi_thread['lifetime'] = pdi_thread['lifetime'] / np.timedelta64(1, 'D')

# reodering the columns
pdi_thread = pdi_thread[['author', 'title', 'thread_comment', 'replies', 'views', 'post_date',
                         'last_replied_date', 'lifetime']]

# data type check
print(pdi_thread.dtypes)

# saving the DataFrame
pdi_thread.to_csv('pdi_thread.csv', sep=",", index=False)
