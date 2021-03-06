from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__, template_folder='template')

with open('questions.json') as file:
    questions = json.load(file)
answers = []
messages = []


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
@app.route('/start', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for('form', i=1))
    else : return render_template('index.html')

@app.route('/form/<i>', methods=["GET", "POST"])
def form(i):
    if request.method == "POST":
        answers.append(request.form.get("question"))
        if questions[f'question{str(int(i)+1)}'] != " ":
            return redirect(url_for('form', i=str(int(i) + 1)))
        else:
            return redirect(url_for('success', chatbot_id='abcdef'))
    else:
        return render_template("question.html",
                               question=questions[f'question{i}'])

@app.route('/success/<chatbot_id>', methods=["GET"])
def success(chatbot_id):
    return render_template('success.html', chatbot_id=chatbot_id, answers=answers)

@app.route('/try_it_now/', methods=["GET", "POST"])
def try_it_now():
    if request.method == "POST":
        message = request.form.get("new_message")
        messages.append(message)
        messages.append('user')
        return render_template('try_it.html', messages=messages, len=len(messages))
    return render_template('try_it.html', messages=messages, len=len(messages))

@app.route('/add_new_question/', methods=["GET", "POST"])
def add_new_question():
    pass

app.run()
