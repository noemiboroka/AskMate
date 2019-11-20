from flask import Flask, render_template, request, redirect, url_for
from AskMate import data_manager
from AskMate import util

app = Flask(__name__)

filename_questions = "ask-mate-python-master/sample_data/question.csv"
filename_answers = "ask-mate-python-master/sample_data/answer.csv"

question_data_table = data_manager.read_file(filename_questions)
answers_data_table = data_manager.read_file(filename_answers)

question_id_list = [row[0] for row in question_data_table[1:]]
answer_id_list = [row[0] for row in answers_data_table[1:]]

@app.route('/')
@app.route('/list')
def route_list():
    questions_data_table = data_manager.read_file(filename_questions)

    return render_template('display_page.html', data_table = questions_data_table)

@app.route("/question/<question_id>")
def question_display(question_id):

    list_of_answers = []
    asked_question = None
    question_message = None

    for row in question_data_table:

        if row[0] == question_id:
            asked_question = row[4]
            question_message = row[5]

    for row in answers_data_table:
        if row[3] == question_id:
            list_of_answers.append(row)


    return render_template('display_question.html',question = asked_question, q_message = question_message, answers = list_of_answers )

@app.route('/add_question', methods=["POST", "GET"])
def add_question():
    new_id = util.det_new_id(question_id_list)
    new_question_list = [new_id]
    for num in range(3):
        new_question_list.append("0")

    if request.method == "POST":
        new_question_list.append(request.form.get('title'))
        new_question_list.append(request.form.get('message'))
        new_question_list.append(" ")

        question_data_table.append(new_question_list)

        data_manager.write_file(filename_questions, question_data_table)
        return redirect('/'
                        '')

    return render_template('add_question.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )


#print(data_manager.read_file(filename))