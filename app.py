from flask import Flask, render_template, request
from quiz_logic import get_quiz  # Import get_quiz function

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for session management


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input", methods=["GET", "POST"])
def user_input():
    if request.method == "POST":
        days = request.form["days"] # Convert days to integer
        subject = request.form["subject"]
        goal = request.form["goal"]

        # Validate user input (optional)
        if not days or not subject or not goal:
            return render_template("input.html", error="Please fill in all fields.")

        # Call get_quiz function with validated input
        questions, answers = get_quiz(days, subject, goal)
        return render_template("quiz.html", questions=questions, answers=answers)

    return render_template("input.html")

@app.route("/quiz", methods=["POST"])
def submit_quiz():
    if request.method == "POST":
        user_answers = request.form.to_dict(flat=False)  # Get user answers as a dictionary

        # Process user answers (e.g., calculate score) using results and correct answers
        # (logic for get_quiz() is assumed to return questions and correct answers)
        score = 0  # Placeholder for calculating score based on user_answers and correct answers
        return render_template("my_page.html")

    return "Invalid request method"  # Handle unexpected access


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Page Not Found"), 404


