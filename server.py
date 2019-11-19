from flask import Flask, render_template, request, redirect, url_for
from ask_mate_python import data_manager

app = Flask(__name__)
filename = "/home/szpoti/codecool/Web/askmate/ask_mate_python/sample_data/question.csv"

data_table = data_manager.read_form_file(filename)

@app.route("/")
@app.route("/list")
def route_list():

    return render_template('display_page.html', data=data_table)

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True
    )
