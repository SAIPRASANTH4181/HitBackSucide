# Importing the required packages
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

class report_word_cloud:
    '''
    Class that takes the aspect based analysed data and presents the report in the form of wordcloud. 
    '''

    def __init__(self,analysed_data):
        self._analysed_data = analysed_data
        
    def word_cloud(self,analysed_data):
        '''
        Definition : Accept the data set after aspect based analysis, and create word cloud for aspects that triggers the sucidies
        : analysed_data : dataframe after the aspect based analysis
        : return        : word cloud displaying the aspect results
        '''

        text = " ".join(review for review in analysed_data.aspect_keywords.astype('string')).lower()
        print (f"There are {len(text)} words in the combination of all review.")

        # Create stopword list:
        stopwords = set(STOPWORDS)

        # Generate a word cloud image
        wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    