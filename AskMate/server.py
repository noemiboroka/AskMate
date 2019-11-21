from flask import Flask, render_template, request, redirect, url_for
import data_manager, util
from datetime import datetime

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
    question_data_table = data_manager.read_file(filename_questions)
    return render_template('display_page.html', data_table = question_data_table)

@app.route("/question/<question_id>")
def question_display(question_id):
    question_data_table = data_manager.read_file(filename_questions)
    answers_data_table = data_manager.read_file(filename_answers)


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


    return render_template('display_question.html',question_id = question_id,question = asked_question, q_message = question_message, answers = list_of_answers )

@app.route('/add_question', methods=["POST", "GET"])
def add_question():
    question_data_table = data_manager.read_file(filename_questions)
    question_id_list = [row[0] for row in question_data_table[1:]]

    new_id = util.det_new_id(question_id_list)
    new_question_list = [new_id]
    timestamp = 1545730073
    time = datetime.fromtimestamp(timestamp)
    new_question_list.append(time)
    for num in range(2):
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

@app.route("/question/<question_id>/new-answer", methods=["POST", "GET"])
def add_new_answer(question_id):
    answers_data_table = data_manager.read_file(filename_answers)
    answer_id_list = [row[0] for row in answers_data_table[1:]]
    if request.method == "POST":
        new_id = util.det_new_id(answer_id_list)
        new_answer_list = [new_id]

        for num in range(2):
            new_answer_list.append("0")
        new_answer_list.append(question_id)
        new_answer_list.append(request.form.get('message'))
        new_answer_list.append(" ")
        answers_data_table.append(new_answer_list)
        data_manager.write_file(filename_answers, answers_data_table)
        return redirect('/'
                        '')

    return render_template('add_answer.html', question_id = question_id)
@app.route('/question/<question_id>/edit', methods=['POST','GET'])
def edit_question(question_id):
    question_data_table = data_manager.read_file(filename_questions)

    if request.method == 'POST':
        for row in question_data_table:
            if row[0] == question_id:
                row[4] = request.form.get('q_title')
                row[5] = request.form.get('q_message')
                data_manager.write_file(filename_questions, question_data_table)
                return redirect(f'/question/{question_id}')

    for row in question_data_table:
        if row[0] == question_id:
            question_title = row[4]
            question_mess = row[5]

    return render_template('edit_question.html', question_id=question_id, question_title = question_title,
                           question_mess = question_mess )


@app.route('/delete/<question_id>')
def delete_question(question_id):
    question_data_table = data_manager.read_file(filename_questions)

    for row in question_data_table:
        if row[0] == question_id:
            question_data_table.remove(row)
            data_manager.write_file(filename_questions, question_data_table)
            return redirect('/')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )


#print(data_manager.read_file(filename))