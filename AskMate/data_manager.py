import csv

#filename = "ask-mate-python-master/sample_data/answer.csv"


def read_file(filename):

    data_table = []

    with open(filename, 'r') as csvFile:
        csvreader = csv.reader(csvFile)

        for row in csvreader:
            data_table.append(row)



    return data_table



def write_file(filename, data_to_write):

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        for row in data_to_write:
            csvwriter.writerow(row)



