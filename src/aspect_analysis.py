import pandas as pd
import numpy as np
from preprocessing import *
from aspect_based_analysis import *
from report_word_cloud import *

class aspect_analysis:
    '''
    Class that calls all the modules for backend processing. It takes preprocessing, aspect based analysis and word cloud for the complete analysis. 
    '''
    
    def __init__(self,data):
        self._data=data

    def end_end_analysis(self,data):
        preprocessed_data=preprocessing.text_preprocessing(data)
        analysed_data=aspect_based_analysis.aspect_analyze(preprocessed_data)
        final_report=report_word_cloud.word_cloud(analysed_data)

        return final_report

