Certainly! To display both the user's answers and the correct answers on the result page, you can modify the code as follows:

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
        is_correct = set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers)

        # Prepare result data including user's answers and correct answers
        result = {
            'question': question['question'],
            'user_answers': user_answers,
            'correct_answers': correct_answers,
            'is_correct': is_correct,
        }
        results.append(result)

        if is_correct:
            score += 1

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
        {% for result in results %}
            <li>
                {{ result['question'] }}
                <ul>
                    <li>Your Answer(s): {{ result['user_answers']|join(', ') }}</li>
                    <li>Correct Answer(s): {{ result['correct_answers']|join(', ') }}</li>
                    {% if result['is_correct'] %}
                        <li><span style="color: green;">(Correct)</span></li>
                    {% else %}
                        <li><span style="color: red;">(Incorrect)</span></li>
                    {% endif %}
                </ul>
            </li>
        {% endfor %}
    </ul>

    <a href="/">Back to Home</a>
</body>
</html>
```

With these modifications, the result page will display both the user's answers and the correct answers for each question, along with whether the user's answer was correct or incorrect.