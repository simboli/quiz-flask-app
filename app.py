from flask import Flask, render_template, request, redirect, url_for, flash, session
import json
import random
import pymysql
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure the MySQL database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'quiz-app'
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
def select_random_questions(questions_list):
    with open('quiz_parameters.json', 'r') as params_file:
        params = json.load(params_file)
        num_questions = params.get('num_questions', 2)  # Default to 2 questions if not specified

    return random.sample(questions_list, num_questions)

@app.route('/')
def index():
    # Select 2 random questions
    selected_questions = select_random_questions(questions)
    session['current_questions'] = selected_questions
    session['session_id'] = generate_session_id()  # Generate a session ID
    session['page_load_time'] = datetime.now()  # Store the page load time

    # Get the total number of questions
    with open('quiz_parameters.json', 'r') as params_file:
        params = json.load(params_file)
        num_questions = params.get('num_questions', 2)  # Default to 2 questions if not specified
        
    # Pass the num_questions variable to the template
    return render_template('index.html', questions=selected_questions, num_questions=num_questions)

# Function to generate a unique session ID
def generate_session_id():
    import uuid
    return str(uuid.uuid4())

@app.route('/submit', methods=['POST'])
def submit():
    # Read passing level from quiz_parameters.json
    with open('quiz_parameters.json', 'r') as params_file:
        params = json.load(params_file)
        passing_level = params.get('passing_level', 0.7)  # Default passing level to 0.7 if not specified
        num_questions = params.get('num_questions', 2)  # Default to 2 questions if not specified
    
    score = 0
    results = []
    selected_questions = session.get('current_questions', [])
    question_number = 1  # Initialize the question number

    cursor = mysql.cursor()
    cursor.execute(
        "INSERT INTO session_info (session_id, page_load_time, submission_time, num_questions, passing_level) VALUES (%s, %s, %s, %s, %s)",
        (session.get('session_id'), session.get('page_load_time'), datetime.now(), num_questions, passing_level)
    )

    for question in selected_questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        
        is_correct = set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers)  # Calculate correctness here
        
        # Save the quiz log for each selected answer with timestamp
        cursor.execute(
            "INSERT INTO quiz_log (session_id, question_number, question_id, question, user_answers, correct_answers, is_correct, first_modified_time, last_modified_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (session.get('session_id'), question_number, question['question_id'], question['question'], '| '.join(user_answers), '| '.join(correct_answers), is_correct, request.form.get("first_modified_" + str(question['question_id'])), request.form.get("last_modified_" + str(question['question_id'])))
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

        question_number += 1  # Increment the question number

    # Commit the changes to the database
    mysql.commit()
    cursor.close()

    return render_template('result.html', score=score, total=len(selected_questions), results=results, passing_level=passing_level, selected_questions=selected_questions)

if __name__ == '__main__':
    app.run(debug=True)