I apologize for the oversight. It appears that the `question_id` column does not exist in your MySQL table. To resolve this issue, you should add the `question_id` column to your MySQL table named `quiz_log`. You can do this with an ALTER TABLE statement:

Here's how you can update your MySQL table to include the `question_id` column:

```sql
ALTER TABLE quiz_log
ADD question_id INT;
```

After adding the `question_id` column to your MySQL table, your app.py code should work without any issues.