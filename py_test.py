import unittest

from src import preprocessing as pre
from src import preprocessing as pre
from src import aspect_based_analysis as aba
from src import report_word_cloud as rwc
from src import aspect_analysis as asa

class TestSum(unittest.TestCase):
    def testing_preprocessing(self):
        """
        Testing the preprocessed data 
        """
        raw_data=""
        preprocessed_obj=pre.preprocessing(raw_data)
        return preprocessed_obj.text_preprocessing()

    def testing_analysis(self):
        '''
        Testing the analysis data
        '''
        preprocessed_data=""
        aspect_based_analysis_obj = aba.aspect_based_analysis(preprocessed_data)
        return aspect_based_analysis_obj.aspect_analyze()
        
    def testing_reporting(self):
        '''
        Testing the reporting data
        '''
        analysed_data=""
        report_word_cloud_obj=rwc.report_word_cloud(analysed_data)
        return report_word_cloud_obj.word_cloud()

    def backend_flow(self):
        '''
        Testing complete workflow
        '''
        DataFrame=""
        aspect_analysis_obj = asa.aspect_analysis(DataFrame)
        return aspect_analysis_obj.end_end_analysis()
        

if __name__ == '__main__':
    unittest.main()

