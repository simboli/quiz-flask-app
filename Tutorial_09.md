I apologize for the oversight. You are correct; the result page should only display the questions that were part of the user's quiz, which in this case is two questions. To fix this issue, you can update the result page to iterate over the selected questions only. Here's the corrected `templates/result.html` file:

**templates/result.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Result</title>
</head>
<body>
    <h1>Quiz Result</h1>
    <h2>Your score: {{ score }}/{{ total }}</h2>
   
    <h3>Questions:</h3>
    <ul>
        {% for selected_question in selected_questions %}
            <li>
                {{ selected_question['question'] }}
                {% for result in results %}
                    {% if result['question'] == selected_question['question'] %}
                        {% if result['correct'] %}
                            <span style="color: green;">(Correct)</span>
                        {% else %}
                            <span style="color: red;">(Incorrect)</span>
                        {% endif %}
                    {% endif %}
                {% endfor %}
            </li>
        {% endfor %}
    </ul>

    <a href="/">Back to Home</a>
</body>
</html>
```

This corrected code ensures that the result page only displays the questions that were part of the user's quiz, matching the selected random questions.