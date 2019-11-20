from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)
filename = data_handler.DATA_FILE_PATH

@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()

    return render_template('list.html', user_stories=user_stories)

@app.route('/story', methods=['GET', 'POST'])
def route_add_story():
    print('a')
    list_of_names = ["story_title", "user_story", "acceptance_criteria", "business_value", "estimation"]
    user_inputs = []
    if request.method == 'POST':
        for title in list_of_names:
            user_inputs.append(request.form.get(title))
        print(user_inputs)
        write_to_file(filename, user_inputs)
        return redirect("/")


    return render_template('add_user_story.html')

def write_to_file(filename, user_inputs):
    with open(filename, "a") as file:
        file.write(','.join(user_inputs))



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
