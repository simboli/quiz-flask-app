You're absolutely right; my previous code doesn't handle questions with multiple correct answers correctly. To support multiple correct answers for a question, you can modify the `questions.json` file to store the correct answers as an array. Here's how you can update the `questions.json` file:

```json
[
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answers": ["Paris"]
    },
    {
        "question": "Which planets are known as the Gas Giants?",
        "choices": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answers": ["Jupiter", "Saturn"]
    },
    {
        "question": "What are the primary colors?",
        "choices": ["Red", "Green", "Blue", "Yellow"],
        "correct_answers": ["Red", "Blue", "Yellow"]
    }
]
```

Now, let's update the Flask application code in `app.py` to handle multiple correct answers:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load questions from JSON file
with open('questions.json', 'r') as file:
    questions = json.load(file)

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        if set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers):
            score += 1
    flash(f'Your score: {score}/{len(questions)}', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

Now, the code correctly handles questions with multiple correct answers by comparing the sets of user answers and correct answers while also checking that they have the same length. This ensures that all correct choices must be selected by the user for the answer to be considered correct.