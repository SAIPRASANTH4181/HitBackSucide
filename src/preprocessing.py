# Importing the required packages
import pandas as pd
from textblob import TextBlob
import re
import string
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import nltk

class preprocessing:
    ''' 
    Class for preprocessing the raw data. It removes the urls, html, emojis and punctuations
    ''' 

    def __init__(self, raw_data):
        '''
        raw_data        : The data that is being uploaded through the portal
        '''
        self._raw_data = raw_data

    def remove_URL(self,headline_text):
        '''
        headline_text   : the raw data 
        return          : data without url
        '''
        url = re.compile(r'https?://\S+|www\.\S+')
        
        return url.sub(r'', headline_text)

    def remove_html(self,headline_text):
        '''
        headline_text   : the data after url removal
        return          : data after removing html
        '''
        html=re.compile(r'<.*?>')
        
        return html.sub(r'',headline_text)

    def remove_emojis(self,data):
        '''
        headline_text   : the data after html removal
        return          : data after removing emojis
        '''
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

    def remove_punct(self,headline_text):
        '''
        headline_text   : the data after emojis removal
        return          : data after removing punctuations
        '''
        table=str.maketrans('','',string.punctuation)
        
        return headline_text.translate(table)

    def text_preprocessing(self,raw_data):
        '''
        raw_data        : the data after pucntuation removal
        return          : the cleaned data after preprocessing the raw data by removing the url,html,emojis and punctuations
        '''
        raw_data['content']=raw_data['content'].apply(self.remove_URL)
        raw_data['content']=raw_data['content'].apply(self.remove_html)
        raw_data['content']=raw_data['content'].apply(self.remove_emojis)
        raw_data['content']=raw_data['content'].apply(self.remove_punct)        
        
        return raw_data