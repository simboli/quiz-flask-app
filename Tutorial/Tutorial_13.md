To save each session and the given answers into a MySQL table log, you will need to integrate Flask-SQLAlchemy to work with MySQL databases. Here's how you can modify your existing code to achieve this:

1. Install Flask-SQLAlchemy:

   You can install Flask-SQLAlchemy using pip:

   ```bash
   pip install Flask-SQLAlchemy
   ```

2. Set up your MySQL database:

   Create a MySQL database and a table to store the quiz log. You can use a tool like phpMyAdmin or run SQL commands to create the database and table. Here's a simple SQL command to create a table:

   ```sql
   CREATE TABLE quiz_log (
       id INT AUTO_INCREMENT PRIMARY KEY,
       session_id VARCHAR(255),
       question VARCHAR(255),
       user_answers TEXT,
       correct_answers TEXT,
       is_correct BOOLEAN
   );
   ```

3. Modify your `app.py` to integrate Flask-SQLAlchemy and log the quiz results:

**app.py:**
```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import json
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/quiz_db'
db = SQLAlchemy(app)

# Define the QuizLog model for the database table
class QuizLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255))
    question = db.Column(db.String(255))
    user_answers = db.Column(db.Text)
    correct_answers = db.Column(db.Text)
    is_correct = db.Column(db.Boolean)

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

    for question in selected_questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        is_correct = set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers)

        # Save the quiz log to the database
        quiz_log = QuizLog(
            session_id=session.get('session_id'),
            question=question['question'],
            user_answers=', '.join(user_answers),
            correct_answers=', '.join(correct_answers),
            is_correct=is_correct
        )
        db.session.add(quiz_log)

        results.append({
            'question': question['question'],
            'user_answers': user_answers,
            'correct_answers': correct_answers,
            'is_correct': is_correct,
        })

        if is_correct:
            score += 1

    # Commit the changes to the database
    db.session.commit()

    return render_template('result.html', score=score, total=len(selected_questions), results=results, selected_questions=selected_questions)

if __name__ == '__main__':
    app.run(debug=True)
```

In this updated code:

- We configure the MySQL database using Flask-SQLAlchemy and define a `QuizLog` model to represent the table where the quiz logs will be stored.
- The `submit` route now logs the quiz results into the MySQL database using the `QuizLog` model.
- We commit the changes to the database using `db.session.commit()`.

Make sure to replace `'mysql://username:password@localhost/quiz_db'` with your actual MySQL database connection URL.

This code will save each session and each given answer into the `quiz_log` table in your MySQL database.