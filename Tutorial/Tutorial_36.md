To display the total number of questions in the quiz, you can use the `num_questions` variable from your Flask app in the `index.html` template. Here's how you can update the template to show the total number of questions:

```html
<!-- Update the index.html template -->
<!DOCTYPE html>
<html>

<head>
    <title>Quiz App</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='css/style.css') }}">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>

<body>
    <div class="container mt-5">
        <div class="d-flex justify-content-center row">
            <div class="col-md-10 col-lg-10">
                <div class="border">
                    <div class="question bg-white p-3 border-bottom">
                        <div class="d-flex flex-row justify-content-between align-items-center mcq">
                            <h4>MCQ Quiz</h4>
                            <span>1 of {{ num_questions }}</span> <!-- Display total number of questions here -->
                        </div>
                        <form method="POST" action="/submit">
                            {% for question in questions %}
                    </div>
                    <div class="question bg-white p-3 border-bottom" id="{{ question['question_id'] }}">
                        <div class="d-flex flex-row align-items-center question-title">
                            <h3 class="text-danger">Q.</h3>
                            <h5 class="mt-1 ml-2">{{ question['question'] }}</h5>
                        </div>
                        <div class="ans ml-2">
                            {% for choice in question['choices'] %}
                            <label class="radio"> <input type="checkbox" class="form-check-input"
                                    name="{{ question['question'] }}" value="{{ choice }}" id="{{ choice }}"> <span>{{
                                    choice }}</span>
                            </label>
                            {% endfor %}
                        </div>
                        <input type="hidden" name="first_modified_{{ question['question_id'] }}" id="first_modified_{{ question['question_id'] }}" value="{{ current_timestamp }}">
                        <input type="hidden" name="last_modified_{{ question['question_id'] }}" id="last_modified_{{ question['question_id'] }}" value="{{ current_timestamp }}">
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-4">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
        </form>
    </div>

    <!-- Update the JavaScript code in your HTML template -->
    <script>
        $(document).ready(function () {
            $("input[type='checkbox']").change(function () {
                // Find the closest question div to the changed checkbox
                var questionDiv = $(this).closest('.question');

                // Get the question ID from the question div
                var questionId = questionDiv.attr('id');

                // Find the hidden input field for firstModifiedField and lastModifiedField
                var firstModifiedField = $("#first_modified_" + questionId);
                var lastModifiedField = $("#last_modified_" + questionId);

                // Check if the firstModifiedField is empty before updating
                if (!firstModifiedField.val()) {
                    // Update the first modified timestamp for this question
                    var now = new Date().toISOString().slice(0, 19).replace('T', ' ');
                    firstModifiedField.val(now);
                }

                // Update the last modified timestamp for this question
                var now = new Date().toISOString().slice(0, 19).replace('T', ' ');
                lastModifiedField.val(now);
            });

            $("#submit-button").click(function () {
                $("#quiz-form").submit();
            });
        });
    </script>

</body>

</html>
```

By adding `{{ num_questions }}` in the `<span>` element, it will display the total number of questions in your quiz as specified in your Flask app's `num_questions` variable.