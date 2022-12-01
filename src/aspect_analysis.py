import pandas as pd
import numpy as np
from src import preprocessing as pre
from src import aspect_based_analysis as aba
from src import report_word_cloud as rwc
class aspect_analysis:
    '''
    Class that calls all the modules for backend processing. It takes preprocessing, aspect based analysis and word cloud for the complete analysis. 
    '''
    
    def __init__(self,data):
        self._data=data

    def end_end_analysis(self):
        print('qqqqqqqqqqqqqqqqq')
        print(self._data)
        preprocessed_obj=pre.preprocessing(self._data)
        preprocessed_data=preprocessed_obj.text_preprocessing()
        #preprocessed_data=preprocessing.text_preprocessing(self._data)
        aspect_based_analysis_obj = aba.aspect_based_analysis(preprocessed_data)
        analysed_data=aspect_based_analysis_obj.aspect_analyze()
        #analysed_data=aspect_based_analysis.aspect_analyze(preprocessed_data)
        report_word_cloud_obj=rwc.report_word_cloud(analysed_data)
        final_report=report_word_cloud_obj.word_cloud()
        #final_report=report_word_cloud.word_cloud(analysed_data)

        return final_report


def main(DataFrame):
    aspect_analysis_obj = aspect_analysis(DataFrame)
    aspect_analysis_obj.end_end_analysis()
    print('pppppppppppppppppp')