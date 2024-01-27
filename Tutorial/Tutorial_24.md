To save the last datetime when the user modifies the state (selected or not selected) of each question, you can update the code in `app.py` to track and record these timestamps. You'll need to make changes in the JavaScript part of your HTML template to capture user interactions and then send these timestamps to the server when the user submits the form. Here's how you can do it:

1. Update your HTML template (`index.html`) to include JavaScript code to track user interactions:

```html
<!DOCTYPE html>
<html>

<head>
    <!-- ... (your existing head content) ... -->
</head>

<body>
    <div class="container mt-5">
        <div class="d-flex justify-content-center row">
            <div class="col-md-10 col-lg-10">
                <div class="border">
                    <div class="question bg-white p-3 border-bottom">
                        <!-- ... (your existing code) ... -->
                        <form method="POST" action="/submit" id="quiz-form">
                            {% for question in questions %}
                            <!-- Add a hidden input field to store the last modified timestamp for each question -->
                            <input type="hidden" name="last_modified_{{ question['question_id'] }}" id="last_modified_{{ question['question_id'] }}" value="">
                            {% endfor %}
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-4">
            <button type="button" class="btn btn-primary" id="submit-button">Submit</button>
        </div>
    </div>

    <!-- Add JavaScript to track user interactions and update last modified timestamps -->
    <script>
        $(document).ready(function () {
            // Handle checkbox changes
            $("input[type='checkbox']").change(function () {
                var questionId = $(this).closest('.question').attr('id');
                var lastModifiedField = $("#last_modified_" + questionId);
                lastModifiedField.val(new Date().toISOString()); // Update the last modified timestamp
            });

            // Handle form submission
            $("#submit-button").click(function () {
                // Submit the form when the user clicks the submit button
                $("#quiz-form").submit();
            });
        });
    </script>
</body>

</html>
```

In this code:

- We've added hidden input fields for each question to store the last modified timestamp (`last_modified_{{ question['question_id'] }}`).
- We've included JavaScript code that listens for changes in the checkboxes (user interactions). When a checkbox is changed, it updates the corresponding hidden input field with the current timestamp.

2. Update your `app.py` to retrieve and store the last modified timestamps in the `quiz_log` table:

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
        
        for answer in user_answers:
            # Save the quiz log for each selected answer with timestamp
            cursor.execute(
                "INSERT INTO quiz_log (session_id, question_id, question, user_answers, correct_answers, is_correct, answer_time, last_modified_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (session.get('session_id'), question['question_id'], question['question'], answer, answer, answer in correct_answers, datetime.now(), request.form.get("last_modified_" + str(question['question_id'])))
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
```

In this updated code:

- We've added a hidden input field for each question in the HTML template to store the last modified timestamp.
- The JavaScript code tracks changes in the checkboxes and updates the corresponding hidden input field with the current timestamp when a change occurs.
- When processing the form submission in `app.py`, we retrieve the last modified timestamp for each question and store it in the `quiz_log` table along with other information.

With these changes, you'll be able to record the last modified timestamps for each question in the `quiz_log` table when the user interacts with the checkboxes.