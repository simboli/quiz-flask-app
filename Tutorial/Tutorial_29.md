To include the question number in the `quiz_log` table, you can modify the code as follows:

1. Add a variable to keep track of the question number.
2. Increment the question number for each question in the loop.
3. Include the question number when inserting data into the `quiz_log` table.

Here's the modified `app.py` script with these changes:

```python
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []
    selected_questions = session.get('current_questions', [])
    question_number = 1  # Initialize the question number

    cursor = mysql.cursor()

    # Save the session information to the database
    cursor.execute(
        "INSERT INTO session_info (session_id, page_load_time, submission_time) VALUES (%s, %s, %s)",
        (session.get('session_id'), session.get('page_load_time'), datetime.now())
    )

    for question in selected_questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        
        is_correct = set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers)  # Calculate correctness here
        
        # Save the quiz log for each selected answer with timestamp
        cursor.execute(
            "INSERT INTO quiz_log (session_id, question_number, question_id, question, user_answers, correct_answers, is_correct, answer_time, last_modified_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (session.get('session_id'), question_number, question['question_id'], question['question'], ', '.join(user_answers), ', '.join(correct_answers), is_correct, datetime.now(), request.form.get("last_modified_" + str(question['question_id'])))
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

    return render_template('result.html', score=score, total=len(selected_questions), results=results, selected_questions=selected_questions)
```

In this code:

- We initialize `question_number` to 1 before the loop.
- Inside the loop, we include `question_number` when inserting data into the `quiz_log` table, which represents the number of the question in the quiz.
- After processing each question, we increment `question_number` to move on to the next question.

This modification will include the question number in the `quiz_log` table for each question, starting from 1 for the first question and incrementing for each subsequent question.