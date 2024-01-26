To modify the application to select only 2 random questions from the list of available questions, you can use the `random` module in Python. Here's the updated `app.py` code:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load questions from JSON file
with open('questions.json', 'r') as file:
    questions = json.load(file)

# Function to select 2 random questions
def select_random_questions(questions_list, num_questions=2):
    return random.sample(questions_list, num_questions)

@app.route('/')
def index():
    # Select 2 random questions
    selected_questions = select_random_questions(questions, num_questions=2)
    return render_template('index.html', questions=selected_questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []
    for question in questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        if set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers):
            score += 1
            results.append({'question': question['question'], 'correct': True})
        else:
            results.append({'question': question['question'], 'correct': False})

    return render_template('result.html', score=score, total=len(questions), results=results)

if __name__ == '__main__':
    app.run(debug=True)
```

With this modification, the `select_random_questions` function is called in the `index` route to select 2 random questions from the list of available questions. The quiz will now display only these 2 random questions for the user to answer.