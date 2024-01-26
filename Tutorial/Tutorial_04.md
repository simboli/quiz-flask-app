Certainly! To display the final score at the top of the result page, you can modify the `templates/result.html` file as follows:

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

This modification adds the final score (e.g., "Your score: 3/5") at the top of the result page, followed by the individual question results.