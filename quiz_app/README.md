# Quiz App

A simple quiz application built using Django. This app allows users to take a quiz, view results, and track their score.

## Prerequisites

To run this project, you need to have Python and Django installed. Follow these steps to set up the project and run it on your local machine.

### Step 1: Clone the repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/quiz-app.git
cd quiz-app
Step 2: Set up Python Environment
Ensure you have Python installed on your machine. You can download the latest version of Python from python.org.

After installing Python, create a virtual environment in the project directory:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On MacOS/Linux:
bash
Copy code
source venv/bin/activate
Step 3: Install dependencies
With the virtual environment activated, install the required dependencies by running:

bash
Copy code
pip install -r requirements.txt
This will install Django and any other dependencies specified in the requirements.txt file.

Step 4: Apply Migrations
Run the following commands to apply database migrations:

bash
Copy code
python manage.py migrate
This will create the necessary database tables for the app.

Step 5: Run the development server
To start the Django development server, run:

bash
Copy code
python manage.py runserver
You should now be able to access the app by going to http://127.0.0.1:8000/ in your browser.

Step 6: Access the Application
Dashboard: View your quiz statistics (questions attempted, correct answers, score).
Quiz: Take a quiz with random questions.
Result: View the result of your quiz attempt and see the correct answers.
Step 7: Stopping the server
To stop the development server, press Ctrl+C in the terminal.

Requirements
Python 3.x
Django 5.1.3

bash
Copy code
pip install -r requirements.txt
Troubleshooting
Ensure that you have Python 3.x installed and activated the virtual environment before running the project.
If you encounter any issues with migrations or database errors, try running python manage.py makemigrations before python manage.py migrate.
License
This project is licensed under the MIT License - see the LICENSE file for details.