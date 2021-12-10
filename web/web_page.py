from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__, template_folder='template')

with open('questions.json') as file:
    questions = json.load(file)
answers = []

@app.route('/<i>', methods=["GET", "POST"])
def form(i):
    if request.method == "POST":
        answers.append(request.form.get("question"))
        return redirect(url_for(f'/{i+1}'))
    return render_template("question.html", question=questions[f"question{i}"])

app.run()
print(answers)
