import csv

filename = "/home/szpoti/codecool/Web/askmate/ask_mate_python/sample_data/question.csv"


def read_form_file(filename):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        data_table = [row for row in csvreader]
    return data_table


def write_to_file(filename,data_table):
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in data_table:
            csvwriter.writerow(row)
