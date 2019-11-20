from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/req_counter')
def route_req_counter():
    #user_stories = data_handler.get_all_user_story()

    return render_template('req_counter.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )