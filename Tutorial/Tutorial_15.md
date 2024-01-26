Certainly! You can modify the app to include the `question_id` and `session_id` when storing quiz logs in the MySQL table. Here's the updated `app.py` code:

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
import json
import random
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure the MySQL database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'quiz_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Create a MySQL database connection
mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB'],
    cursorclass=pymysql.cursors.DictCursor
)

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
    session['current_questions'] = selected_questions
    session['session_id'] = generate_session_id()  # Generate a session ID
    return render_template('index.html', questions=selected_questions)

# Function to generate a unique session ID
def generate_session_id():
    import uuid
    return str(uuid.uuid4())

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []
    selected_questions = session.get('current_questions', [])

    cursor = mysql.cursor()

    for question in selected_questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        is_correct = set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers)

        # Save the quiz log to the database
        cursor.execute(
            "INSERT INTO quiz_log (session_id, question_id, question, user_answers, correct_answers, is_correct) VALUES (%s, %s, %s, %s, %s, %s)",
            (session.get('session_id'), question['question_id'], question['question'], ', '.join(user_answers), ', '.join(correct_answers), is_correct)
        )

        results.append({
            'question_id': question['question_id'],
            'question': question['question'],
            'user_answers': user_answers,
            'correct_answers': correct_answers,
            'is_correct': is_correct,
        })

        if is_correct:
            score += 1

    # Commit the changes to the database
    mysql.commit()
    cursor.close()

    return render_template('result.html', score=score, total=len(selected_questions), results=results, selected_questions=selected_questions)

if __name__ == '__main__':
    app.run(debug=True)
```

In this updated code:

- We added a `generate_session_id` function to create a unique session ID using the `uuid` library.
- When storing quiz logs in the database, we include the `question_id` and `session_id`.
- The session ID is generated and stored in the `session` dictionary, ensuring each session has a unique identifier.

Please replace `'username'`, `'password'`, and other database connection details with your actual MySQL database credentials.