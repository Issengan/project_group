import csv 

def read_csv_file(file_path):

    data = [] 

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        headers = next(csv_reader) 

        for row in csv_reader: 
            data.append(dict(zip(headers, row))) 
          
    return data 
