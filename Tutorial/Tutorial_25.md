Certainly! Here's the CREATE TABLE script for the `quiz_log` table, including the `last_modified_time` column:

```sql
CREATE TABLE quiz_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(255),
    question_id INT,
    question VARCHAR(255),
    user_answers TEXT,
    correct_answers TEXT,
    is_correct BOOLEAN,
    answer_time DATETIME,
    last_modified_time DATETIME
);
```

This script creates the `quiz_log` table with the following columns:

- `id`: A unique identifier for each log entry.
- `session_id`: Stores the session ID associated with the quiz.
- `question_id`: The ID of the question.
- `question`: The question text.
- `user_answers`: The user's selected answer(s).
- `correct_answers`: The correct answer(s).
- `is_correct`: A flag indicating if the user's answer(s) are correct.
- `answer_time`: The timestamp when the user answered the question.
- `last_modified_time`: The timestamp representing the last modification time for the question's state (selected or not selected).

Make sure to execute this SQL script in your database to create the `quiz_log` table with the specified columns.