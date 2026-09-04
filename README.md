# 🏥 AI Hospital Management System

> A web-based hospital management system built with **Python, Flask, SQLite, HTML/CSS, and Machine Learning** to simplify hospital administration and provide AI-assisted disease prediction.

![AI Hospital Management System](screenshots/dashboard.png)

## 📌 Overview

The **AI Hospital Management System** is a full-stack web application designed to manage essential hospital operations through a simple and user-friendly interface.

The system combines traditional hospital management features with a machine-learning-based disease prediction module.

It provides dedicated sections for:

* 👨‍⚕️ Doctor management
* 👤 Patient management
* 📅 Appointment management
* 🤖 AI-based disease prediction
* 📊 Hospital administration dashboard
* 🗄️ SQLite database storage

The project was developed as an academic/portfolio project to demonstrate practical skills in **Python, Flask, databases, web development, and machine learning integration**.

---

## ✨ Features

### 📊 Hospital Dashboard

The dashboard provides a centralized overview of the hospital system.

It displays:

* Number of doctors
* Number of patients
* Number of appointments
* Recent appointments
* Navigation to major hospital services

![Hospital Dashboard](screenshots/dashboard.png)

---

### 👨‍⚕️ Doctor Management

The doctor section provides information about doctors available in the hospital.

Each doctor can have information such as:

* Doctor name
* Specialization
* Experience

![Doctors](screenshots/doctors.png)

---

### 👤 Patient Management

The patient section provides a simple interface for displaying patient information.

Example patient information includes:

* Patient name
* Age
* Medical condition

![Patients](screenshots/patients.png)

---

### 📅 Appointment Management

The appointment module allows users to create and view hospital appointments.

Appointment information includes:

* Patient name
* Doctor
* Appointment date
* Appointment time

Appointments are stored in a **SQLite database**.

![Appointments](screenshots/appointments.png)

---

### 🤖 AI Disease Prediction

The system includes a machine-learning module that predicts a possible disease based on selected symptoms.

The prediction system accepts symptoms such as:

* Fever
* Cough
* Headache
* Fatigue

The trained machine-learning model processes the selected symptoms and returns a predicted disease.

![AI Disease Prediction](screenshots/prediction.png)

> **Note:** This prediction feature is intended for educational and demonstration purposes and should not be used as a substitute for professional medical diagnosis.

---

## 🧠 Machine Learning

The project uses a trained machine-learning model for disease prediction.

The model files are stored inside the `model/` directory:

```text
model/
├── disease_model.pkl
├── label_encoder.pkl
└── train_model.py
```

### Training Workflow

The general workflow is:

```text
Symptoms Dataset
       ↓
Data Preparation
       ↓
Model Training
       ↓
Trained Model
       ↓
Flask Application
       ↓
User Symptoms
       ↓
Disease Prediction
```

The trained model is loaded by Flask using `joblib`.

---

## 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Backend programming       |
| Flask        | Web application framework |
| SQLite       | Database management       |
| HTML5        | Web page structure        |
| CSS3         | User interface styling    |
| Scikit-learn | Machine learning          |
| Joblib       | Model serialization       |
| CSV          | Dataset storage           |
| Git & GitHub | Version control           |

---

## 📁 Project Structure

```text
ai-hospital-management-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── symptoms.csv
│
├── model/
│   ├── disease_model.pkl
│   ├── label_encoder.pkl
│   └── train_model.py
│
└── templates/
    ├── appointments.html
    ├── dashboard.html
    ├── doctors.html
    ├── index.html
    ├── patients.html
    └── prediction.html
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/munnakalyani/ai-hospital-management-system.git
```

### 2. Open the project directory

```bash
cd ai-hospital-management-system
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

The application should start on:

```text
http://127.0.0.1:5000
```

Open the address in your web browser.

---

## 🗄️ Database

The application uses **SQLite** for appointment data.

The database is automatically initialized by the Flask application.

The database contains an `appointments` table with fields such as:

```text
id
patient_name
doctor
appointment_date
appointment_time
```

The local database file is excluded from Git using `.gitignore`.

---

## 📊 Dataset

The machine-learning component uses the dataset stored at:

```text
dataset/symptoms.csv
```

The dataset contains symptom information used to train the disease prediction model.

---

## 🔐 Security & Privacy

This project is intended as an educational demonstration.

For a production hospital system, additional security features would be required, including:

* User authentication
* Role-based access control
* Password hashing
* Secure session management
* Input validation
* Database security
* Encryption of sensitive patient information
* Audit logging
* Healthcare privacy and compliance controls

No real patient information should be used in a public deployment of this project.

---

## 🚀 Future Improvements

Potential improvements include:

* 🔐 Secure doctor and patient login
* 👥 Role-based authentication
* 📝 Patient medical history
* 💊 Prescription management
* 🧪 Laboratory report management
* 💳 Billing and payment management
* 📧 Appointment notifications
* 📱 Responsive mobile interface
* 📈 Hospital analytics and reports
* ☁️ Cloud deployment
* 🗃️ PostgreSQL/MySQL database support
* 🔒 Improved security and privacy controls
* 🧠 More advanced machine-learning models

---

## 🎯 Learning Objectives

This project demonstrates practical experience with:

* Python programming
* Flask web development
* REST-style routing
* HTML/CSS interfaces
* SQLite database operations
* CRUD-style appointment management
* Machine-learning model integration
* Model serialization using Joblib
* Git version control
* GitHub project management

---

## 👩‍💻 Author

**munnakalyani**

GitHub:
https://github.com/munnakalyani

---

## 📄 License

This project is intended primarily for educational and portfolio purposes.

If you plan to distribute or modify the project as open-source software, consider adding an appropriate open-source license.
## 📸 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Doctors
![Doctors](screenshots/doctors.png)

### Patients
![Patients](screenshots/patients.png)

### Appointments
![Appointments](screenshots/appointments.png)

### AI Disease Prediction
![AI Disease Prediction](screenshots/prediction.png)
---


