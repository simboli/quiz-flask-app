To save the `num_questions` and `passing_level` from `quiz_parameters.json` into the `session_info` table, you can modify your `app.py` script as follows:

1. Update your `app.py` to read and save `num_questions` and `passing_level` into the `session_info` table:

```python
# ... (previous code)

@app.route('/')
def index():
    # Select 2 random questions
    selected_questions = select_random_questions(questions)
    session['current_questions'] = selected_questions
    session['session_id'] = generate_session_id()  # Generate a session ID
    session['page_load_time'] = datetime.now()  # Store the page load time

    # Read quiz parameters from quiz_parameters.json
    with open('quiz_parameters.json', 'r') as params_file:
        params = json.load(params_file)
        num_questions = params.get('num_questions', 2)  # Default to 2 questions if not specified
        passing_level = params.get('passing_level', 0.7)  # Default to 0.7 if not specified

    # Save quiz parameters to the session_info table
    cursor = mysql.cursor()
    cursor.execute(
        "INSERT INTO session_info (session_id, page_load_time, submission_time, num_questions, passing_level) VALUES (%s, %s, %s, %s, %s)",
        (session.get('session_id'), session.get('page_load_time'), datetime.now(), num_questions, passing_level)
    )
    mysql.commit()
    cursor.close()

    return render_template('index.html', questions=selected_questions)

# ... (rest of the code)
```

2. You will also need to modify your `CREATE TABLE` statement for the `session_info` table to include the `num_questions` and `passing_level` fields. Here's an updated `CREATE TABLE` statement:

```sql
CREATE TABLE session_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(255) NOT NULL,
    page_load_time DATETIME NOT NULL,
    submission_time DATETIME NOT NULL,
    num_questions INT NOT NULL,
    passing_level FLOAT NOT NULL
);
```

Ensure that you have this table structure in your MySQL database to save the `num_questions` and `passing_level` values.

With these changes, the `num_questions` and `passing_level` values from `quiz_parameters.json` will be saved in the `session_info` table when a new session is created.