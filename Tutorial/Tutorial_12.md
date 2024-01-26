Certainly! You can add Bootstrap to your HTML pages for a better look and responsiveness. Here's how you can update your HTML files:

1. First, you need to include Bootstrap CSS and JavaScript files in your HTML files. You can link to them by adding the following lines to the `<head>` section of your HTML files:

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
```

2. Update your HTML files to use Bootstrap classes for styling and responsiveness. Here's how you can update `index.html` and `result.html`:

**index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz App</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Quiz App</h1>
        <form method="POST" action="/submit">
            {% for question in questions %}
                <div class="card mt-4">
                    <div class="card-header">{{ question['question'] }}</div>
                    <div class="card-body">
                        {% for choice in question['choices'] %}
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" name="{{ question['question'] }}" value="{{ choice }}" id="{{ choice }}">
                                <label class="form-check-label" for="{{ choice }}">{{ choice }}</label>
                            </div>
                        {% endfor %}
                    </div>
                </div>
            {% endfor %}
            <div class="mt-4">
                <button type="submit" class="btn btn-primary">Submit</button>
            </div>
        </form>
    </div>
</body>
</html>
```

**result.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Result</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Quiz Result</h1>
        <h2>Your score: {{ score }}/{{ total }}</h2>

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

These updates will apply Bootstrap styles and improve the look and responsiveness of your quiz application's pages.