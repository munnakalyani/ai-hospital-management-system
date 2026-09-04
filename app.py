
from flask import Flask, render_template, request
import joblib
import os
import sqlite3

app = Flask(__name__)

# AI model
model = joblib.load(
    os.path.join("model", "disease_model.pkl")
)

encoder = joblib.load(
    os.path.join("model", "label_encoder.pkl")
)


# ---------------- DATABASE ----------------

def init_db():
    conn = sqlite3.connect("hospital.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            doctor TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------------- HOME ----------------

@app.route("/")
def index():
    return render_template("index.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- DOCTORS ----------------

@app.route("/doctors")
def doctors():
    return render_template("doctors.html")


# ---------------- PATIENTS ----------------

@app.route("/patients")
def patients():
    return render_template("patients.html")


# ---------------- APPOINTMENTS ----------------

@app.route("/appointments", methods=["GET", "POST"])
def appointments():

    conn = sqlite3.connect("hospital.db")

    if request.method == "POST":

        patient_name = request.form.get("patient_name")
        doctor = request.form.get("doctor")
        appointment_date = request.form.get("appointment_date")
        appointment_time = request.form.get("appointment_time")

        conn.execute("""
            INSERT INTO appointments
            (patient_name, doctor, appointment_date, appointment_time)
            VALUES (?, ?, ?, ?)
        """, (
            patient_name,
            doctor,
            appointment_date,
            appointment_time
        ))

        conn.commit()

    appointments_data = conn.execute("""
        SELECT patient_name, doctor, appointment_date, appointment_time
        FROM appointments
        ORDER BY appointment_date, appointment_time
    """).fetchall()

    conn.close()

    return render_template(
        "appointments.html",
        appointments=appointments_data
    )


# ---------------- AI PREDICTION ----------------

@app.route("/prediction", methods=["GET", "POST"])
def prediction():

    result = None

    if request.method == "POST":

        fever = int(request.form.get("fever", 0))
        cough = int(request.form.get("cough", 0))
        headache = int(request.form.get("headache", 0))
        fatigue = int(request.form.get("fatigue", 0))

        symptoms = [[
            fever,
            cough,
            headache,
            fatigue
        ]]

        prediction_value = model.predict(symptoms)[0]

        try:
            result = encoder.inverse_transform(
                [prediction_value]
            )[0]
        except Exception:
            result = prediction_value

    return render_template(
        "prediction.html",
        result=result
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)