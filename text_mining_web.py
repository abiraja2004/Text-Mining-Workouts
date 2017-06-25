
# coding: utf-8

# ### Text Mining from Website
# 
# Hi, In this iPython Workbook, we will look into extracting data from a Webpage using commonly available libraries and cleaning the data.
# 
# **Start_Date:** 20 - June
# 
# **End_Date:**  25 - June
# 
# **Python_Version:** 2.7

# In[1]:

# Importing the required libraries
# JSON and CSV Modules
# NLTK <- for common stopwords
# Importing Beautiful Soup for HTML Parser
import csv
import nltk
import string
from urllib import urlopen
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


# In[2]:

# Installing URL
url = "https://en.wikipedia.org/wiki/Chennai"

# Reading the webpage
web = urlopen(url)


# ##### Tags have commonly used names that depend on their position in relation to other tags:
# 
# **child** – a child is a tag inside another tag. So the two p tags above are both children of the body tag.
# 
# **parent** – a parent is the tag another tag is inside. Above, the html tag is the parent of the body tag.
# 
# **sibiling** – a sibiling is a tag that is nested inside the same parent as another tag. For example, head and body are siblings, since they’re both inside html. Both p tags are siblings, since they’re both inside body.

# In[3]:

# Downloading the webpage
webpage = requests.get(url)

print "Webpage Download: ", webpage

# The Response code of <- 200 represents that the webpage has been downloaded successfully.
# Printing the contents of the Downloaded webpage
print "\nContent Print: ",webpage.content[:101]


# In[4]:

# Using Beautiful Soup to parse the Webpage.
soup = bs(webpage.content, 'html.parser')

# Printing the HTML Content using Prettify method
print (soup.prettify())


# In[5]:

# Since, we have used Beautiful Soup, all the tags are nested and
# print out the specific tags <- Children
list(soup.children)


# ##### The above tells us that there are two tags at the top level of the page – the initial <!DOCTYPE html> tag, and the html tag. There is a newline character (\n) in the list as well.

# In[6]:

# Type of each element
[type(item) for item in list(soup.children)] 


# ##### As you can see, all of the items are BeautifulSoup objects. The first is a Doctype object, which contains information about the type of the document. The second is a NavigableString, which represents text found in the HTML document. The final item is a Tag object, which contains other nested tags. The most important object type, and the one we’ll deal with most often, is the Tag object.

# In[7]:

# Now, finding all <p>, in the webpage.
soup.find_all('p')


# In[8]:

soup.find_all('p')[10].get_text()


# #### Searching for tags by class and id:
# 
# Classes and ids are used by CSS to determine which HTML elements to apply certain styles to. We can also use them when scraping to specify specific elements we want to scrape.

# In[9]:

# Using BS4, we can also search specifically using class
soup.find_all(class_='reference')[10]


# In[10]:

# Using id
soup.find_all(id="cite_ref-4")


# #### Extracting Data from a Webpage - Weather Data to Pandas Dataframe
# 
# In this example, we will mine for weather data and convert it into pandas dataframe and finally will do some analysis in it.

# In[11]:

# Extracting Weather Data <- Online Web portal <- Chennai
page = requests.get("https://www.theweathernetwork.com/in/weather/tamil-nadu/chennai")
soup = bs(page.content, 'html.parser')
# We initialize our data from id and class_ as worked out earlier.
seven_day = soup.find(id="seven-days")
forecast_items = seven_day.find_all(class_="seven-days-only")
daily = forecast_items[0]
print(daily.prettify())


# #### Extracting information from the page
# 
# Now, let's consider extracting information from the page:
# 
# * Forecast Item name - Mon <- class <- "day_name"
# * Day Outlook - class <- "day_outlook" <- Mainly Cloudy
# * High Temperature - class <- "chart-daily-temp seven_days_metric seven_days_metric_c" <- 33 C

# In[12]:

# Checking for our known Attributes!!
# Day, Outlook and Temperature
day = daily.find(class_="day_name").get_text()
day_outlook = daily.find(class_="day_outlook").get_text()
temp = daily.find(class_="chart-daily-temp seven_days_metric seven_days_metric_c").get_text()

print "Forecast Day: ", day
print "Day's Outlook: ", day_outlook
print "Highest Temp: ", temp


# #### Since, we have obtained data for only one particular day, we now extract for all days.
# 
# Also, note that the Outlook has \t attached and hence, we source the information from img alt

# In[13]:

# Extracting for Days
days_tags = seven_day.select(".seven-days-only .day_name")
days = [pt.get_text() for pt in days_tags]
days


# In[14]:

# Extracting for Temperature in Celcius
temp_tags = seven_day.select(".seven-days-only .chart-daily-temp.seven_days_metric.seven_days_metric_c")
temp = [t.get_text() for t in temp_tags]
temp


# In[15]:

# Removing the \t spaces in temperature
out = [x[1:5] for x in temp]
out


# In[16]:

# Obtaining the Description/Outlook from the image file
img = daily.find("img")
desc = img['title']

print desc


# In[17]:

# Obtaining the Outlook for all the Seven Days
outlook = [t["title"] for t in seven_day.select(".seven-days-only img")]

print outlook


# In[18]:

# Combining into Pandas Dataframe.
import pandas as pd
weather = pd.DataFrame({
        "Days": days, 
        "Temperature": out,
        "Outlook": outlook
    })
weather


# In[19]:

# Now, checking the dataypes of the above dataframe
weather.dtypes


# In[20]:

# Converting the Temperature to a integer type
temp_nums = weather["Temperature"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
temp_nums


# In[21]:

# Finding the Mean
weather["temp_num"].mean()

