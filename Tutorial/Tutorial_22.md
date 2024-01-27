Understood! If you want to record the timestamp when the user selects each answer for each question, you can update the script accordingly. You'll need to create a separate entry in the `quiz_log` table for each answer selected by the user. Here's how you can modify the code:

1. Update the `quiz_log` table structure to include an `answer_time` column:

   ```sql
   ALTER TABLE quiz_log
   ADD answer_time DATETIME;
   ```

2. Modify the `app.py` code to record the timestamp for each answer:

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
import json
import random
import pymysql
from datetime import datetime

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
    session['page_load_time'] = datetime.now()  # Store the page load time
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

    # Save the session information to the database
    cursor.execute(
        "INSERT INTO session_info (session_id, page_load_time, submission_time) VALUES (%s, %s, %s)",
        (session.get('session_id'), session.get('page_load_time'), datetime.now())
    )

    for question in selected_questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        
        for answer in user_answers:
            # Save the quiz log for each selected answer with timestamp
            cursor.execute(
                "INSERT INTO quiz_log (session_id, question_id, question, user_answers, correct_answers, is_correct, answer_time) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (session.get('session_id'), question['question_id'], question['question'], answer, answer, answer in correct_answers, datetime.now())
            )

        results.append({
            'question_id': question['question_id'],
            'question': question['question'],
            'user_answers': user_answers,
            'correct_answers': correct_answers,
            'is_correct': set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers),
        })

        if set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers):
            score += 1

    # Commit the changes to the database
    mysql.commit()
    cursor.close()

    return render_template('result.html', score=score, total=len(selected_questions), results=results, selected_questions=selected_questions)

if __name__ == '__main__':
    app.run(debug=True)
```

In this updated code:

- For each selected answer by the user, we create a separate entry in the `quiz_log` table with the timestamp when the user selected that answer.
- We iterate through the `user_answers` list for each question and insert each answer separately into the `quiz_log` table with the corresponding timestamp.
- This ensures that you record the timestamp for each answer selection by the user for each question.

Make sure to adjust your database table structure accordingly using the ALTER TABLE statement mentioned earlier.