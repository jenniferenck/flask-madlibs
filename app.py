from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
# REVIEW THIS ^^^^^^

# VIEW functions go here...


@app.route("/")
def display_questions():
    """loop through list provided in instance and generate a form from each"""

    prompts = story.prompts
    # takes prompts from story instance and sets in list

    return render_template("form.html", prompts=prompts)


@app.route("/story", methods=["POST"])
def show_result():
    """invoke generate func and pass answers into story html """

    result = request.form  # generates a list of key-value pairs in tuples
    print(result)
    text = story.generate(request.form)
    # pass results into class function to generate key val pairs

    return render_template("story.html", text=text)
