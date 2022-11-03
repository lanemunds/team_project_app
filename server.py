from flask import Flask, render_template, redirect, url_for

from forms import TeamForm

app = Flask(__name__)
app.secret_key = "keep this secret"

@app.route("/")
def home():
    team_form = TeamForm()
    return render_template('home.html', team_form = team_form)

@ app.route("/add-team", methods = ["POST"])
def add_team():
    team_form = TeamForm()
    
    if team_form.validate_on_submit():
        print(team_form.team_name.data)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug = True)