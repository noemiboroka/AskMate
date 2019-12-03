"""
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
"""

import database_common
import time


@database_common.connection_handler
def read_all_questions(cursor):
    cursor.execute("""
                    SELECT * FROM question;
                    """)
    questions = cursor.fetchall()
    return questions


@database_common.connection_handler
def read_a_question(cursor, id_):
    cursor.execute("""
                    SELECT * FROM question WHERE id=%(id_)s;
                    """, {'id_': id_})
    questions = cursor.fetchall()
    return questions


@database_common.connection_handler
def answer_by_question_id(cursor, id_):
    cursor.execute("""
                    SELECT * FROM answer WHERE question_id=%(id_)s;
                    """, {'id_': id_})
    answers = cursor.fetchall()
    return answers


@database_common.connection_handler
def add_question(cursor, new_question):
    cursor.execute("""
                        INSERT INTO question(id, submission_time, view_number, vote_number, title, message, image) 
                        VALUES (%(id)s,%(submission_time)s, %(view_number)s, %(vote_number)s,%(title)s,%(message)s,
                        %(image)s);
                        """, new_question)


def sorted_by_submission_time(list_of_dicts):
    n = len(list_of_dicts)
    for i in range(n):
        for j in range(i, n):
            if list_of_dicts[j]['submission_time'] > list_of_dicts[i]['submission_time']:
                temp = list_of_dicts[i]
                list_of_dicts[i] = list_of_dicts[j]
                list_of_dicts[j] = temp
    return list_of_dicts


def get_new_question_id():
    questions = read_all_questions()
    max_id = "0"
    for i in questions:
        if int(max_id) < int(i['id']):
            max_id = i['id']
    max_id = int(max_id) + 1
    return str(max_id)


def convert_time(unix_timestamp):
    readable_time = time.ctime(int(unix_timestamp))
    return readable_time


def get_current_unix_timestamp():
    current_time = time.time()
    return int(current_time)
