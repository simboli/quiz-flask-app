CREATE TABLE `quiz_log` (
  `id` int NOT NULL,
  `session_id` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `question_number` int DEFAULT NULL,
  `question_id` int DEFAULT NULL,
  `question` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `user_answers` text COLLATE utf8mb4_general_ci,
  `correct_answers` text COLLATE utf8mb4_general_ci,
  `is_correct` tinyint(1) DEFAULT NULL,
  `first_modified_time` datetime DEFAULT NULL,
  `last_modified_time` datetime DEFAULT NULL
);

ALTER TABLE `quiz_log`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `quiz_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

CREATE TABLE `session_info` (
  `id` int NOT NULL,
  `session_id` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `page_load_time` datetime NOT NULL,
  `submission_time` datetime NOT NULL,
  `num_questions` int NOT NULL,
  `passing_level` float NOT NULL
);

ALTER TABLE `session_info`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `session_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
