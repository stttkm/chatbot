from flask import Flask, request, render_template
import json

app = Flask(__name__, template_folder='template')

with open('questions.json') as file:
    questions = json.load(file)
answers = []


for i in questions.keys():
    @app.route(f'/{i}', methods=["GET", "POST"])
    def form():
        if request.method == "POST":
            answers.append(request.form.get("question"))
            return render_template("question.html",
                                   question=questions[i]["question"],
                                   hint=questions[i]["hint"],
                                   next="Next")
app.run()
print(answers)
