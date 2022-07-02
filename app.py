from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template ("index.html")


@app.route('/project', methods=['POST', 'GET'])
def Project_f():
    return render_template ("Project.html")


@app.route('/Net', methods=['POST', 'GET'])
def Net():
    return render_template ("Net.html")


@app.route('/Neuralweb', methods=['POST', 'GET'])
def Neuralweb():
    return render_template ("Neuralweb.html")


@app.route('/Sitecard', methods=['POST', 'GET'])
def Sitecard():
    return render_template ("Site_card.html")


if __name__ == '__main__':
    app.run()
