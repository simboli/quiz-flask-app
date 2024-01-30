# Free open source Quiz App (Flask and MySQL)

The Quiz App is an open-source web application built with Python and Flask that allows users to take quizzes and assess your knowledge. It's designed to be easy to use, customizable, and can be adapted for various educational or assessment purposes.

![Screenshot 1](screenshot/Screen_001.png?raw=true "Screenshot 1")

## Introduction

The Quiz App provides a user-friendly interface for creating and taking quizzes. Whether you're an educator looking to create quizzes for your students or an enthusiast wanting to test your knowledge, this app is designed to meet your needs. It offers features like random question selection, user response recording, and real-time scoring.

## Database Structure

The Quiz App uses a MySQL database to store questions, quiz logs, and session information. Below are the descriptions of the fields in the main files and tables:


### Questions Table (file `questions.json`)

- `question_id` (Primary Key): Unique identifier for each question.
- `question`: The actual quiz question.
- `correct_answers`: Comma-separated list of correct answers.
- `choices`: Comma-separated list of answer choices.

### Parameter Table (file `quiz_parameters.json`)

- `num_questions`: Number of question of each takes.
- `passing_level`: The actual passing level.
- `quiz_title`: The title of the quiz, it will be printed on the top of the quiz page.

### Quiz Log Table

- `log_id` (Primary Key): Unique identifier for each quiz log entry.
- `session_id` (Foreign Key): Links the log entry to a specific quiz session.
- `question_number`: The order of the question in the quiz session.
- `question_id`: The ID of the question from the Questions table.
- `question`: The text of the question.
- `user_answers`: User's selected answers, separated by a pipe (|).
- `correct_answers`: Correct answers for the question, separated by a pipe (|).
- `is_correct`: Indicates whether the user's answers were correct (1 for correct, 0 for incorrect).
- `first_modified_time`: Timestamp of the first modification to the question.
- `last_modified_time`: Timestamp of the last modification to the question.

### Session Info Table

- `session_id` (Primary Key): Unique identifier for each quiz session.
- `page_load_time`: Timestamp when the user loaded the quiz page.
- `submission_time`: Timestamp when the user submitted the quiz.
- `num_questions`: Number of questions in the quiz session.
- `passing_level`: The passing score required to pass the quiz.

## Python Module Dependencies

To run the Quiz App, you need the following Python modules and dependencies:

- **Flask:** A web framework for Python.
- **pymysql:** A Python library for connecting to MySQL databases.
- **Jinja2:** for rendering HTML templates.
- **Bootstrap:** for styling.

You can install these dependencies via pip using the following command:

```bash
pip install Flask pymysql
```

## Getting Started

To get started with the Quiz App, follow these steps:

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/simboli/quiz-flask-app.git
   ```

2. Create a virtual environment and install the required dependencies.

   ```bash
   cd quiz-app
   python -m venv Quizvenv
   source Quizvenv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Configure the MySQL database settings in `app.py`:

   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'your_username'
   app.config['MYSQL_PASSWORD'] = 'your_password'
   app.config['MYSQL_DB'] = 'quiz-app'
   ```

4. Import the database schema using the provided SQL script in `database.sql`.

   ```bash
   mysql -u your_username -p quiz-app < database.sql
   ```

5. Run the Flask application.

   ```bash
   python app.py
   ```

6. Access the Quiz App in your web browser at `http://localhost:5000`.

## Customization

You can customize the Quiz App by:

- Adding or modifying questions in the `questions.json` file.
- Adjusting the passing level and number of questions in `quiz_parameters.json`.
- Modifying the HTML templates in the `templates` directory.
- Styling the application by editing the `style.css` file.

## Contributing

Contributions to the Quiz App are welcome! If you'd like to add new features, fix bugs, or improve the documentation, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes and push them to your fork.

   ```bash
   git commit -m "Add your feature"
   git push origin feature/your-feature-name
   ```

4. Create a pull request on the main repository.

## Future Improvements

Here are some enhancements and features that can be added to the Flask Quiz App in the nearly future:

1. **Enhanced Styling:** Improve the overall style and visual design of the application for a more appealing user interface.

2. **Better Accessibility:** Ensure that the application is accessible to users with disabilities, following accessibility standards.

3. **Enhanced Responsive Experience:** Make the app more mobile-friendly and responsive for a seamless experience on smartphones and tablets.

4. **Support for Code and Graphics:** Allow quiz creators to include code snippets and images in questions and answer choices.

5. **User Authentication:** Implement user authentication and user account management for personalized quiz creation and tracking.

6. **Leaderboards:** Add a leaderboard feature to display high scores and rankings for quizzes.

7. **Timer for Quizzes:** Introduce a timer option for quizzes, adding a time constraint for each question.

8. **Export Quiz Results:** Enable users to export their quiz results in various formats, such as PDF or CSV.

9. **Multi-Language Support:** Support multiple languages to make the app accessible to a global audience.

10. **User Feedback:** Collect user feedback and suggestions for continuous improvement.

We welcome contributions from the open-source community to help implement these enhancements and make the Flask Quiz App even better!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.