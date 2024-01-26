I apologize for the oversight. To display only the questions that were part of the user's quiz on the result page, you need to modify the code further. You can pass the selected questions along with their results to the template. Here's the corrected `app.py` and `result.html` files:

**app.py:**
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
    selected_questions = select_random_questions(questions, num_questions=2)

    for question in selected_questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        if set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers):
            score += 1
            results.append({'question': question['question'], 'correct': True})
        else:
            results.append({'question': question['question'], 'correct': False})

    return render_template('result.html', score=score, total=len(selected_questions), results=results, selected_questions=selected_questions)

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/result.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Result</title>
</head>
<body>
    <h1>Quiz Result</h1>
    <h2>Your score: {{ score }}/{{ total }}</h2>
   
    <h3>Questions:</h3>
    <ul>
        {% for selected_question in selected_questions %}
            <li>
                {{ selected_question['question'] }}
                {% for result in results %}
                    {% if result['question'] == selected_question['question'] %}
                        {% if result['correct'] %}
                            <span style="color: green;">(Correct)</span>
                        {% else %}
                            <span style="color: red;">(Incorrect)</span>
                        {% endif %}
                    {% endif %}
                {% endfor %}
            </li>
        {% endfor %}
    </ul>

    <a href="/">Back to Home</a>
</body>
</html>
```

With these corrections, the result page should correctly display only the questions that were part of the user's quiz, matching the selected random questions.