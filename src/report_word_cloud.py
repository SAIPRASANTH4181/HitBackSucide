# Importing the required packages
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

import collections
import matplotlib.cm as cm
from matplotlib import rcParams
class report_word_cloud:
    '''
    Class that takes the aspect based analysed data and presents the report in the form of wordcloud. 
    '''

    def __init__(self,analysed_data):
        self._analysed_data = analysed_data
        
    def word_cloud(self):
        '''
        Definition : Accept the data set after aspect based analysis, and create word cloud for aspects that triggers the sucidies
        : analysed_data : dataframe after the aspect based analysis
        : return        : word cloud displaying the aspect results
        '''
        analysed_data=self._analysed_data
        if cleaned_data=="":
            raise Exception("In analysis the data was nullified")
            return print('Reporting exited')
        else:
            print('The analysis was successful and sent the data for reporting')
            pass
        text = " ".join(review for review in analysed_data.aspect_keywords.astype('string')).lower()
        print (f"There are {len(text)} words in the combination of all review.")

        # Create stopword list:
        stopwords = set(STOPWORDS)

        # Generate a word cloud image
        wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        # plt.savefig("myImage.png", format="png", dpi=1200)
        # plt.figure(figsize=(5, 5))
        plt.axis("off")
        # plt.show()
        wordcloud =  wordcloud.to_file('N2.png')

        filtered_words = [word for word in text.split() if word not in stopwords]
        counted_words = collections.Counter(filtered_words)
        words = []
        counts = []
        print('--------------dadadd-------------------')
        for letter, count in counted_words.most_common(11):
            if letter[:2]=="['":
                words.append(letter[2:])
            
            elif letter[-2:]=="']":
                words.append(letter[:-2]) 

            else:
                words.append(letter)      
            
            counts.append(count)
            print(words)
            print(counts)
        print('--------------dadadd----hggfhdgsfsdgfhjk---------------')    
        colors = cm.rainbow(np.linspace(0, 1, 10))
        rcParams['figure.figsize'] = 20, 10

        plt.title('Top words in the headlines vs their count')
        plt.xlabel('Count')
        plt.ylabel('Words')
        plt.bar(words, counts, color=colors)

        return [words[1:],counts[1:]]