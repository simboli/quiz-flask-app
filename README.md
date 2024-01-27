This is the readme file.

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
  ```sql
   CREATE TABLE session_info (
       id INT AUTO_INCREMENT PRIMARY KEY,
       session_id VARCHAR(255),
       page_load_time DATETIME,
       submission_time DATETIME
   );
   ```