from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template ("main.html")


@app.route('/project', methods=['POST', 'GET'])
def Project_f():
    return render_template ("Project.html")


if __name__ == '__main__':
    app.run()
