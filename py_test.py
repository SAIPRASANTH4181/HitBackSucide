from src import preprocessing as pre
from src import preprocessing as pre
from src import aspect_based_analysis as aba
from src import report_word_cloud as rwc
from src import aspect_analysis as asa


def testing_preprocessing():
    '''
    Testing the preprocessed data 
    '''
    raw_data=""
    preprocessed_obj=pre.preprocessing(raw_data)
    return preprocessed_obj.text_preprocessing()

def testing_analysis():
    '''
    Testing the analysis data
    '''
    preprocessed_data=""
    aspect_based_analysis_obj = aba.aspect_based_analysis(preprocessed_data)
    return aspect_based_analysis_obj.aspect_analyze()
    
def testing_reporting():
    '''
    Testing the reporting data
    '''
    analysed_data=""
    report_word_cloud_obj=rwc.report_word_cloud(analysed_data)
    return report_word_cloud_obj.word_cloud()

def backend_flow():
    '''
    Testing complete workflow
    '''
    DataFrame=""
    aspect_analysis_obj = asa.aspect_analysis(DataFrame)
    return aspect_analysis_obj.end_end_analysis()
    

def end_end_workflow_testing():
    print(testing_preprocessing)
    print(testing_analysis)
    print(testing_reporting)
    print(backend_flow)
    print('Testcases ended')

