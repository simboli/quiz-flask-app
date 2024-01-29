To calculate and display whether the quiz is "Passed!" or "Not passed" based on the `passing_level` read from the `quiz_parameters.json` file, you can modify the `result.html` template as follows:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Result</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Quiz Result</h1>   
        <h2>Your score: {{ score }}/{{ total }}</h2>

        {% with passing_level = 0.7 %} {# Default passing level if not specified #}
        {% include 'quiz_parameters.json' %}
        {% endwith %}

        {% if score/total >= passing_level %}
            <h3 class="text-success">Passed!</h3>
        {% else %}
            <h3 class="text-danger">Not passed</h3>
        {% endif %}

        <h3>Questions:</h3>
        <ul class="list-group mt-3">
            {% for result in results %}
                <li class="list-group-item">
                    {{ result['question'] }}
                    <ul class="list-group mt-2">
                        <li class="list-group-item">Your Answer(s): {{ result['user_answers']|join(', ') }}</li>
                        <li class="list-group-item">Correct Answer(s): {{ result['correct_answers']|join(', ') }}</li>
                        {% if result['is_correct'] %}
                            <li class="list-group-item text-success">(Correct)</li>
                        {% else %}
                            <li class="list-group-item text-danger">(Incorrect)</li>
                        {% endif %}
                    </ul>
                </li>
            {% endfor %}
        </ul>

        <a href="/" class="btn btn-primary mt-4">Back to Home</a>
    </div>
</body>
</html>
```

In this modification:

1. We calculate the `passing_level` from the `quiz_parameters.json` file and set a default value of 0.7 if not specified.
2. We use an `{% if ... %}` statement to check if the score ratio is greater than or equal to the `passing_level`.
3. Depending on the result, we display "Passed!" in green or "Not passed" in red.

This modification will dynamically show the appropriate pass/fail message based on the `passing_level` defined in the `quiz_parameters.json` file.