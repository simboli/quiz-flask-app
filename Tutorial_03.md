I apologize for the oversight. To display the quiz results, you can update the `submit` route in `app.py` to render the `result.html` template with the score. Here's the updated code:

```python
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []
    for question in questions:
        user_answers = request.form.getlist(question['question'])
        correct_answers = question['correct_answers']
        if set(user_answers) == set(correct_answers) and len(user_answers) == len(correct_answers):
            score += 1
            results.append({'question': question['question'], 'correct': True})
        else:
            results.append({'question': question['question'], 'correct': False})

    return render_template('result.html', score=score, total=len(questions), results=results)
```

Now, let's update the `templates/result.html` file to display the results:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Result</title>
</head>
<body>
    <h1>Quiz Result</h1>
    <p>Your score: {{ score }}/{{ total }}</p>
   
    <h2>Questions:</h2>
    <ul>
        {% for result in results %}
            <li>
                {{ result['question'] }}
                {% if result['correct'] %}
                    <span style="color: green;">(Correct)</span>
                {% else %}
                    <span style="color: red;">(Incorrect)</span>
                {% endif %}
            </li>
        {% endfor %}
    </ul>

    <a href="/">Back to Home</a>
</body>
</html>
```

With these updates, when the user submits the quiz, they will be redirected to the `result.html` page, which displays their score and indicates which questions they answered correctly and incorrectly.