import csv
import json

def convert_file_format(input_file_path: str, output_file_path: str,
                        input_format: str = 'csv', output_format: str = 'json'):

    csvfile = open(input_file_path,'r', encoding='utf-8')
    jsonfile = open(output_file_path, 'w',encoding='utf-8')
    fieldnames = ('name','age','gender','class','score')
    
    reader = csv.DictReader( csvfile, fieldnames)
    out = json.dumps( [ row for row in reader ] ,ensure_ascii=False)
    jsonfile.write(out)

