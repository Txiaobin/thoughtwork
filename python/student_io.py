import pandas as pd
'''
def convert_file_format(input_file_path: str, output_file_path: str,
                        input_format: str = 'csv', output_format: str = 'json'):

'''
f = pd.read_csv('student.csv')
f.to_json('newstudent.json')