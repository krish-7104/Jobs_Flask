from flask import Flask, render_template, redirect, request, jsonify, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from database import load_jobs, load_job, add_application, get_applications, get_applicant_details, get_user_by_username
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')  
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    user = get_user_by_username(user_id) 
    if user:
        return User(user_id)
    return None

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=load_jobs())

@app.route("/job/<id>")
def show_job(id):
    return render_template("job.html", job=load_job(id))
    
@app.route("/apply/<id>", methods=["GET"])
def apply_form(id):
    return render_template("application_form.html", job=load_job(id))

@app.route("/apply/<id>", methods=["POST"])
def submit_form(id):
    form_data = dict(request.form)
    result = add_application(form_data, id)
    if result['status']:
        return redirect("/thankyou")

@app.route("/thankyou", methods=["GET"])
def thankyou():
    return render_template("thankyou.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = get_user_by_username(username)  
        if user and user['password'] == password:  
            login_user(User(username))
            return redirect("/admin/applications")
    return render_template("login.html")

@app.route("/admin/applications", methods=["GET"])
@login_required
def applications_admin():
    return render_template("applications.html", applications=get_applications())

@app.route("/admin/application/<id>", methods=["GET"])
@login_required
def applicant_details_admin(id):
    return render_template("applicant_details.html", applicant=get_applicant_details(id))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
