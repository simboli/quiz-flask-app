You are correct; MySQLdb is no longer supported for Python 3.x. PyMySQL is a good alternative for working with MySQL databases in Python 3.x. To use PyMySQL in your Flask application, you can follow these steps:

1. Install PyMySQL:

   You can install PyMySQL using pip:

   ```bash
   pip install pymysql
   ```

2. Modify your `app.py` code to use PyMySQL:

**app.py:**
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
    return render_template('index.html', questions=selected_questions)

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
            "INSERT INTO quiz_log (session_id, question, user_answers, correct_answers, is_correct) VALUES (%s, %s, %s, %s, %s)",
            (session.get('session_id'), question['question'], ', '.join(user_answers), ', '.join(correct_answers), is_correct)
        )

        results.append({
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

- We configure the MySQL database connection using the PyMySQL library.
- We create a MySQL database connection using the configured settings.
- The `submit` route now logs the quiz results into the MySQL database using SQL queries executed through the PyMySQL cursor.
- We commit the changes to the database using `mysql.commit()`, and close the cursor when done.

Please replace `'username'`, `'password'`, and other database connection details with your actual MySQL database credentials.