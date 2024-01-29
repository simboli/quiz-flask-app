To read the `num_questions` parameter from a `quiz_parameters.json` file, you can make the following modifications:

1. Create a `quiz_parameters.json` file with the desired structure and values.
2. Modify the `select_random_questions` function to read the `num_questions` parameter from the JSON file.

Here's how you can do it:

### `quiz_parameters.json` Structure:

```json
{
    "num_questions": 2
}
```

In this JSON file, you specify the number of questions (`num_questions`) you want to select for each quiz.

### Modified `select_random_questions` Function:

```python
def select_random_questions(questions_list):
    with open('quiz_parameters.json', 'r') as params_file:
        params = json.load(params_file)
        num_questions = params.get('num_questions', 2)  # Default to 2 questions if not specified

    return random.sample(questions_list, num_questions)
```

In this modification:

- We open and read the `quiz_parameters.json` file to obtain the `num_questions` parameter.
- If the `num_questions` parameter is not specified in the JSON file, we default to 2 questions.
- The `num_questions` parameter is then used in the `random.sample` function to select the specified number of questions.

With these changes, you can easily configure the number of questions for each quiz by updating the `num_questions` value in the `quiz_parameters.json` file without modifying the Python code.