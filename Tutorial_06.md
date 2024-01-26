You're absolutely right. To update the result page to display only the questions that were part of the user's quiz, you can modify the `templates/result.html` file. Here's the updated `result.html`:

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
        {% for result in results %}
            {% for question in questions %}
                {% if result['question'] == question['question'] %}
                    <li>
                        {{ question['question'] }}
                        {% if result['correct'] %}
                            <span style="color: green;">(Correct)</span>
                        {% else %}
                            <span style="color: red;">(Incorrect)</span>
                        {% endif %}
                    </li>
                {% endif %}
            {% endfor %}
        {% endfor %}
    </ul>

    <a href="/">Back to Home</a>
</body>
</html>
```

This modification ensures that the result page only displays the questions that were part of the user's quiz, based on the selected random questions.