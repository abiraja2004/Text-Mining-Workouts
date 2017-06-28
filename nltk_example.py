
# coding: utf-8

# ### NLTK Package - Python - Text Mining Tutorial

# **What is NLTK?**
# 
# NLTK is a leading platform for building Python programs to work with human language data. 
# It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, 
# along with a suite of text processing libraries for classification, tokenization, stemming, 
# tagging, parsing, and semantic reasoning.

# ** Python Version: ** Python 2.7
# 
# ** Workbook: ** Jupyter iPython

# In[1]:

# Importing NLTK Package
import nltk
# If there is an import error, please download the NLTK Package.
# nltk.download() <- I have already installed an updated version of NLTK Corpus Data.


# In[2]:

# Testing NLTK
from nltk.corpus import brown
print "Sample Words: ", brown.words()[0:5]
# Checking the length of brown words
print "The Length of Brown Words: ",len(brown.words())


# In[3]:

# Using python's inbuilt function dir(), we find the valid attributes of brown nltk corpus

dir(brown)


# In[4]:

# NLTK has it's own book's available for testing
# Let's check them out.
from nltk.book import *


# In[5]:

# Let's check out the valid attributes of one of the text's.
dir(text5)


# In[6]:

# Let's check out the length of text5 from NLTK package.
print "Length: ", len(text5)

print "Words: ", text5[:10]


# ### Sent Tokenize, Word Tokenize, Pos Tagging
# 
# For any given sentence, how do we tokenize the words to be used as data. Let's take a example sentence from Wikipedia and try to tokenize it using the above mentioned libraries.
# 
# **Packages Used:** sent_tokenize, word_tokenize, pos_tag
# 
# **Sample Text:** Text mining, also referred to as text data mining, roughly equivalent to text analytics, is the process of deriving high-quality information from text. High-quality information is typically derived through the devising of patterns and trends through means such as statistical pattern learning. Text mining usually involves the process of structuring the input text (usually parsing, along with the addition of some derived linguistic features and the removal of others, and subsequent insertion into a database), deriving patterns within the structured data, and finally evaluation and interpretation of the output. 'High quality' in text mining usually refers to some combination of relevance, novelty, and interestingness. Typical text mining tasks include text categorization, text clustering, concept/entity extraction, production of granular taxonomies, sentiment analysis, document summarization, and entity relation modeling (i.e., learning relations between named entities).

# In[7]:

# Importing the required packages
from nltk import sent_tokenize, word_tokenize, pos_tag


# In[8]:

# Input sample text
sample = "Text mining, also referred to as text data mining, roughly equivalent to text analytics, is the process of deriving high-quality information from text. High-quality information is typically derived through the devising of patterns and trends through means such as statistical pattern learning. Text mining usually involves the process of structuring the input text (usually parsing, along with the addition of some derived linguistic features and the removal of others, and subsequent insertion into a database), deriving patterns within the structured data, and finally evaluation and interpretation of the output. 'High quality' in text mining usually refers to some combination of relevance, novelty, and interestingness. Typical text mining tasks include text categorization, text clustering, concept/entity extraction, production of granular taxonomies, sentiment analysis, document summarization, and entity relation modeling (i.e., learning relations between named entities)."


# In[9]:

# Testing Sentence Tokenizer.
s1 = sent_tokenize(sample)
print "Full Output:", s1
print "\nOne Sentence:", s1[1]
print "\nLenght: ", len(s1)


# #### As can be noticed from the above output, the sentence tokenizer splits at each and every sentence. That is where ever it find a full stop(.), it stops and breaks that as a part of the data and inputs into an array.

# In[10]:

# Testing Word Toeknizer.
s2 = word_tokenize(sample)
print "Full Output:", s2
print "\nOne Word:", s2[11]
print "\nLenght: ", len(s2)


# #### As can be noticed from the above output, the word tokenize splits at each and every word. Even commas and full stops are added into different data arrays.

# In[11]:

# Testing Pos Tagging.
# A part-of-speech tagger, or POS-tagger, processes a sequence of words, and attaches a part of speech tag to each word
s3 = pos_tag(s2)
print "Full Output:", s3
print "\nOne Tag:", s3[12]
print "\nLenght: ", len(s3)


# Here,
# 
# **CC <- Coordinating conjunction, NN <- Noun, IN <- Preposition, JJ <- Adjective, VB <- Verbs.**

# ### This being just an introduction, I will be working more on Text Mining Algorithms, which can extract data and these can be used to build up a text classifier and work more progressively using Machine Learning Algorithms.
