To store the datetime when each user answers each question in the `quiz_log` table, you can modify the structure of the table to include an `answer_time` column of type DATETIME. Here's how you can update the table structure:

```sql
ALTER TABLE quiz_log
ADD answer_time DATETIME;
```

With this modification, your `quiz_log` table will have an additional column called `answer_time` to record the datetime when each user answers each question.

Your updated `quiz_log` table structure might look like this:

```sql
CREATE TABLE quiz_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(255),
    question_id INT,
    question VARCHAR(255),
    user_answers TEXT,
    correct_answers TEXT,
    is_correct BOOLEAN,
    answer_time DATETIME
);
```

Make sure to adjust your database table structure accordingly, and update your code to insert the `answer_time` when saving quiz log entries, as shown in the previous code example.