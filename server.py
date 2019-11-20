from flask import Flask, render_template, request, redirect, url_for
from ask_mate_python import data_manager

app = Flask(__name__)
filename = "/home/szpoti/codecool/Web/askmate/ask_mate_python/sample_data/question.csv"

data_table = data_manager.read_form_file(filename)

list_of_ids = [element[0] for element in data_table[1:]]

@app.route("/")
@app.route("/list")
def route_list():

    return render_template('display_page.html', data=data_table)

@app.route("/question/<question_id>")
def question_display(question_id):
    id = None

    if question_id in list_of_ids:
        id = question_id

    return render_template('display_question.html', question_id=question_id, id=id)

if __name__ == '__main__':
    print(f" list of ids: {list_of_ids}")
    app.run(
        port=5000,
        debug=True
    )
