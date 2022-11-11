# Importing the required packages
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

def word_cloud(df):
    '''
    Definition : Accept the data set after aspect based analysis, and create word cloud for aspects that triggers the sucidies
    : df = dataframe after the aspect based analysis
    '''
    text = " ".join(review for review in df.aspect_keywords.astype('string')).lower()
    print (f"There are {len(text)} words in the combination of all review.")

    # Create stopword list:
    stopwords = set(STOPWORDS)

    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def demo_word_cloud():
    print ('Presenting you the word cloud.')

demo_word_cloud()