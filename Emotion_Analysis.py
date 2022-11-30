#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import itertools


# In[3]:


df=pd.read_csv('temp.csv')


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


df.columns


# In[ ]:





# In[ ]:





# In[ ]:





# ## Text Processing

# In[7]:


from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

import nltk
nltk.download('all')


# In[8]:


train_tweets = df.copy()
train_tweets.head()


# In[9]:


# Removing URLs
def remove_URL(headline_text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', headline_text)


# In[10]:


df1=train_tweets.copy()
df1['content']=df1['content'].apply(remove_URL)


# In[11]:


# Removing the html tags
def remove_html(headline_text):
    html=re.compile(r'<.*?>')
    return html.sub(r'',headline_text)


# In[12]:


df1['content']=df1['content'].apply(remove_html)
df1.content.values


# In[13]:


# Removing Pictures/Tags/Symbols/Emojis
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)


# In[14]:


df1['content']=df1['content'].apply(remove_emojis)
df1.content.values


# In[15]:


import string

# Removing punctuations
def remove_punct(headline_text):
    table=str.maketrans('','',string.punctuation)
    return headline_text.translate(table)


# In[16]:


df1['content']=df1['content'].apply(remove_punct)
df1.content.values


# In[17]:


df1.drop(columns=['date'],inplace=True)
refined_data=df1.copy()
refined_data.head()


# In[ ]:





# ## Aspect Based Sentiment Analysis

# In[18]:


import os
#!pip install spacy
import spacy
from tqdm import tqdm
import en_core_web_sm
nlp = en_core_web_sm.load()
toy_rev=df1.copy()


# In[19]:


#!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


# In[20]:


def aspect_based_analysis(toy_rev):
    # toy_rev ---> The final_dataset on which we perform sentiment analysis
    nlp = en_core_web_sm.load()

    # List of emotions that are used to analyze the sentiments
    competitors = ['Depression','Stress','Relationship','Emotions','Finance','Society']
    aspect_terms = []
    comp_terms = []
    easpect_terms = []
    ecomp_terms = []
    enemy = []
    for x in tqdm(range(len(toy_rev['content']))):
        amod_pairs = []
        advmod_pairs = []
        compound_pairs = []
        xcomp_pairs = []
        neg_pairs = []
        eamod_pairs = []
        eadvmod_pairs = []
        ecompound_pairs = []
        eneg_pairs = []
        excomp_pairs = []
        enemlist = []
        if len(str(toy_rev['content'][x])) != 0:
            lines = str(toy_rev['content'][x]).replace('*',' ').replace('-',' ').replace('so ',' ').replace('be ',' ').replace('are ',' ').replace('just ',' ').replace('get ','').replace('were ',' ').replace('When ','').replace('when ','').replace('again ',' ').replace('where ','').replace('how ',' ').replace('has ',' ').replace('Here ',' ').replace('here ',' ').replace('now ',' ').replace('see ',' ').replace('why ',' ').split('.')       
            for line in lines:
                enem_list = []
                for eny in competitors:
                    enem = re.search(eny,line)
                    if enem is not None:
                        enem_list.append(enem.group())
                if len(enem_list)==0:
                    doc = nlp(line)
                    str1=''
                    str2=''
                    for token in doc:
                        if token.pos_ is 'NOUN':
                            for j in token.lefts:
                              if j.dep_ == 'compound':
                                compound_pairs.append((j.text+' '+token.text,token.text))
                                if j.dep_ is 'amod' and j.pos_ is 'ADJ': #primary condition
                                    str1 = j.text+' '+token.text
                                    amod_pairs.append(j.text+' '+token.text)
                                    for k in j.lefts:
                                        if k.dep_ is 'advmod': #secondary condition to get adjective of adjectives
                                            str2 = k.text+' '+j.text+' '+token.text
                                            amod_pairs.append(k.text+' '+j.text+' '+token.text)
                                    mtch = re.search(re.escape(str1),re.escape(str2))
                                    if mtch is not None:
                                        amod_pairs.remove(str1)
                        if token.pos_ is 'VERB':
                            for j in token.lefts:
                                if j.dep_ is 'advmod' and j.pos_ is 'ADV':
                                    advmod_pairs.append(j.text+' '+token.text)
                                if j.dep_ is 'neg' and j.pos_ is 'ADV':
                                  neg_pairs.append(j.text+' '+token.text)
                            for j in token.rights:
                                if j.dep_ is 'advmod'and j.pos_ is 'ADV':
                                    advmod_pairs.append(token.text+' '+j.text)
                        if token.pos_ is 'ADJ':
                            for j,h in zip(token.rights,token.lefts):
                                if j.dep_ is 'xcomp' and h.dep_ is not 'neg':
                                    for k in j.lefts:
                                        if k.dep_ is 'aux':
                                            xcomp_pairs.append(token.text+' '+k.text+' '+j.text)
                                elif j.dep_ is 'xcomp' and h.dep_ is 'neg':
                                    if k.dep_ is 'aux':
                                            neg_pairs.append(h.text +' '+token.text+' '+k.text+' '+j.text)
                
                else:
                    enemlist.append(enem_list)
                    doc = nlp(line)
                    str1=''
                    str2=''
                    for token in doc:
                        if token.pos_ is 'NOUN':
                            for j in token.lefts:
                              if j.dep_ == 'compound':
                                ecompound_pairs.append((j.text+' '+token.text,token.text))
                                if j.dep_ is 'amod' and j.pos_ is 'ADJ': #primary condition
                                    str1 = j.text+' '+token.text
                                    eamod_pairs.append(j.text+' '+token.text)
                                    for k in j.lefts:
                                        if k.dep_ is 'advmod': #secondary condition to get adjective of adjectives
                                            str2 = k.text+' '+j.text+' '+token.text
                                            eamod_pairs.append(k.text+' '+j.text+' '+token.text)
                                    mtch = re.search(re.escape(str1),re.escape(str2))
                                    if mtch is not None:
                                        eamod_pairs.remove(str1)
                        if token.pos_ is 'VERB':
                            for j in token.lefts:
                                if j.dep_ is 'advmod' and j.pos_ is 'ADV':
                                    eadvmod_pairs.append(j.text+' '+token.text)
                                if j.dep_ is 'neg' and j.pos_ is 'ADV':
                                  eadvmod_pairs.append(token.text+' '+j.text)
                        if token.pos_ is 'ADJ':
                            for j in token.rights:
                                if j.dep_ is 'xcomp':
                                    for k in j.lefts:
                                        if k.dep_ is 'aux':
                                            excomp_pairs.append(token.text+' '+k.text+' '+j.text)
            pairs = list(set(amod_pairs+advmod_pairs+neg_pairs+xcomp_pairs))
            epairs = list(set(eamod_pairs+eadvmod_pairs+eneg_pairs+excomp_pairs))
            for i in range(len(pairs)):
                if len(compound_pairs)!=0:
                    for comp in compound_pairs:
                        mtch = re.search(re.escape(comp[1]),re.escape(pairs[i]))
                        if mtch is not None:
                            pairs[i] = pairs[i].replace(mtch.group(),comp[0])
            for i in range(len(epairs)):
                if len(ecompound_pairs)!=0:
                    for comp in ecompound_pairs:
                        mtch = re.search(re.escape(comp[1]),re.escape(epairs[i]))
                        if mtch is not None:
                            epairs[i] = epairs[i].replace(mtch.group(),comp[0])
                
        aspect_terms.append(pairs)
        comp_terms.append(compound_pairs)
        easpect_terms.append(epairs)
        ecomp_terms.append(ecompound_pairs)
        enemy.append(enemlist)
    toy_rev['compound_nouns'] = comp_terms
    toy_rev['aspect_keywords'] = aspect_terms
    toy_rev['competition'] = enemy
    toy_rev['competition_comp_nouns'] = ecomp_terms
    toy_rev['competition_aspects'] = easpect_terms
    
    ## Creating a compound vader score
    cs = []
    for row in range(len(toy_rev)):
        cs.append(sid.polarity_scores(toy_rev['content'].iloc[row])['compound'])
    toy_rev['compound_vader_score'] = cs

    return toy_rev
                          


# In[21]:


xy=aspect_based_analysis(refined_data)
xy


# In[ ]:





# ## Word Cloud

# In[22]:


df=xy.copy()


# In[23]:


from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go

def plotly_wordcloud(text):
    wc = WordCloud(stopwords = set(STOPWORDS),
                   max_words = 20,
                   max_font_size = 10)
    wc.generate(text)
    
    word_list=[]
    freq_list=[]
    fontsize_list=[]
    position_list=[]
    orientation_list=[]
    color_list=[]

    for (word, freq), fontsize, position, orientation, color in wc.layout_:
        word_list.append(word)
        freq_list.append(freq)
        fontsize_list.append(fontsize)
        position_list.append(position)
        orientation_list.append(orientation)
        color_list.append(color)
        
    # get the positions
    x=[]
    y=[]
    for i in position_list:
        x.append(i[0])
        y.append(i[1])
            
    # get the relative occurence frequencies
    new_freq_list = []
    for i in freq_list:
        new_freq_list.append(i*100)
    new_freq_list
    
    trace = go.Scatter(x=x, 
                       y=y, 
                       textfont = dict(size=new_freq_list,
                                       color=color_list),
                       hoverinfo='text',
                       hovertext=['{0}{1}'.format(w, f) for w, f in zip(word_list, freq_list)],
                       mode='text',  
                       text=word_list
                      )
    
    layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
    
    fig = go.Figure(data=[trace], layout=layout)
    
    return fig


# In[24]:


df.columns


# In[25]:


# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
#% matplotlib inline


# In[26]:


text = " ".join(review for review in df.aspect_keywords.astype('string')).lower()
print (f"There are {len(text)} words in the combination of all review.")

# Create stopword list:
stopwords = set(STOPWORDS)

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
from matplotlib import rcParams
rcParams['figure.figsize'] = 10, 20
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
wordcloud =  wordcloud.to_file('N1.png')


# In[27]:


text = " ".join(review for review in df.competition_aspects.astype('string')).lower()
print (f"There are {len(text)} words in the combination of all review.")

# Create stopword list:
stopwords = set(STOPWORDS)

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
rcParams['figure.figsize'] = 10, 20
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
wordcloud =  wordcloud.to_file('N2.png')


#barchart
import collections
import matplotlib.cm as cm
filtered_words = [word for word in text.split() if word not in stopwords]
counted_words = collections.Counter(filtered_words)

words = []
counts = []
for letter, count in counted_words.most_common(10):
    words.append(letter)
    counts.append(count)

colors = cm.rainbow(np.linspace(0, 1, 10))
rcParams['figure.figsize'] = 20, 10

plt.title('Top words in the headlines vs their count')
plt.xlabel('Count')
plt.ylabel('Words')
plt.barh(words, counts, color=colors)