This is the readme file.

```sql
CREATE TABLE `quiz_log` (
  `id` int NOT NULL,
  `session_id` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
   `question_id` int DEFAULT NULL
  `question` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `user_answers` text COLLATE utf8mb4_general_ci,
  `correct_answers` text COLLATE utf8mb4_general_ci,
  `is_correct` tinyint(1) DEFAULT NULL,
);
```
