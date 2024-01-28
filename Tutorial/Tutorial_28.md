I apologize for the oversight. It seems that the `is_correct` variable was mistakenly placed inside the for loop for the `user_answers`. You should define `is_correct` outside of the for loop, as it is not related to each individual user answer but rather to the overall correctness of the answers for a given question.

Here's the corrected `app.py` code:

```python
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
        
        is_correct = set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers)  # Calculate correctness here
        
        for answer in user_answers:
            # Save the quiz log for each selected answer with timestamp
            cursor.execute(
                "INSERT INTO quiz_log (session_id, question_id, question, user_answers, correct_answers, is_correct, answer_time, last_modified_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (session.get('session_id'), question['question_id'], question['question'], ', '.join(user_answers), ', '.join(correct_answers), is_correct, datetime.now(), request.form.get("last_modified_" + str(question['question_id'])))
            )

        results.append({
            'question_id': question['question_id'],
            'question': question['question'],
            'user_answers': user_answers,
            'correct_answers': correct_answers,
            'is_correct': is_correct,  # Assign is_correct to each question
        })

        if is_correct:
            score += 1

    # Commit the changes to the database
    mysql.commit()
    cursor.close()

    return render_template('result.html', score=score, total=len(selected_questions), results=results, selected_questions=selected_questions)
```

I've moved the calculation of `is_correct` outside of the for loop that iterates over the `user_answers`, and now it's calculated once for each question.

This should resolve the `NameError` issue, and your application should work as expected.