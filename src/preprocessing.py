import pandas as pd
from textblob import TextBlob
import re
import string
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
train_tweets = df.copy()
train_tweets.head()
import nltk
nltk.download('all')

def remove_URL(headline_text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', headline_text)


def remove_html(headline_text):
    html=re.compile(r'<.*?>')
    return html.sub(r'',headline_text)

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


# Removing punctuations
def remove_punct(headline_text):
    table=str.maketrans('','',string.punctuation)
    return headline_text.translate(table)




# Function calling all the preprocessing methods
def preprocessing(df):
    df1['content']=df1['content'].apply(remove_URL)
    df1['content']=df1['content'].apply(remove_html)
    df1['content']=df1['content'].apply(remove_emojis)
    df1['content']=df1['content'].apply(remove_punct)
    
    return df1
    
