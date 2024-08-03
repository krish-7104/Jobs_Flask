from flask import Flask, render_template, redirect, request, jsonify
from database import load_jobs, load_job,add_application,get_applications

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=load_jobs())

@app.route("/job/<id>")
def show_job(id):
    return render_template("job.html", job=load_job(id))

@app.route("/applications")
def get_all_application():
    return jsonify(get_applications())
    

@app.route("/apply/<id>", methods=["GET"])
def apply_form(id):
    return render_template("application_form.html", job=load_job(id))

@app.route("/apply/<id>", methods=["POST"])
def submit_form(id):
    form_data = dict(request.form)
    result = add_application(form_data, id)
    if result['status']==True:
        return redirect("/thankyou")

@app.route("/thankyou", methods=["GET"])
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)