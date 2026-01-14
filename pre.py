from flask import Flask, render_template, request
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load("student_pass_model.pkl")
@app.route("/", methods=["GET", "POST"])
def home():
 prediction = None
 study_hours = ""
 attendance = ""
 if request.method == "POST":
 study_hours = request.form["study_hours"]
 attendance = request.form["attendance"]
 pred = model.predict(
 np.array([[float(study_hours),float(attendance)]]))[0]
 prediction = "PASS" if pred == 1 else "FAIL"
 return render_template(
 "index.html",
 prediction=prediction,
 study_hours=study_hours,
 attendance=attendance)
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=7860)