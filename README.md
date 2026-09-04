# 🏥 AI Hospital Management System

A web-based **AI Hospital Management System** built with **Python, Flask, SQLite, HTML, CSS, and Machine Learning**.

The system provides hospital administration features such as doctor management, patient management, appointment scheduling, and AI-assisted disease prediction through a simple web interface.

---

## 🌐 Application Links

> **Local Demo:** Start the Flask application first with `python app.py`.

| Service          | Link                                                    |
| ---------------- | ------------------------------------------------------- |
| 🏠 Home          | [Open Home](http://127.0.0.1:5000/)                     |
| 📊 Dashboard     | [Open Dashboard](http://127.0.0.1:5000/dashboard)       |
| 👨‍⚕️ Doctors    | [Open Doctors](http://127.0.0.1:5000/doctors)           |
| 👤 Patients      | [Open Patients](http://127.0.0.1:5000/patients)         |
| 📅 Appointments  | [Open Appointments](http://127.0.0.1:5000/appointments) |
| 🤖 AI Prediction | [Open AI Prediction](http://127.0.0.1:5000/prediction)  |

### 🚀 Live Demo

**Coming soon — the Flask application will be deployed online.**

After deployment, replace the links above with your public application URL.

For example:

```text
https://your-hospital-app.example.com
```

---

# 📊 Dashboard

The hospital dashboard provides a centralized overview of the system.

It displays:

* 👨‍⚕️ Number of doctors
* 👤 Number of patients
* 📅 Number of appointments
* 📋 Recent appointments
* 🔗 Navigation to hospital services

### Dashboard Screenshot

![Hospital Dashboard](screenshots/dashboard.png)

---

# 👨‍⚕️ Doctors

The Doctors section displays information about available doctors.

Each doctor can have:

* Doctor name
* Specialization
* Experience

### Doctors Screenshot

![Doctors](screenshots/doctors.png)

---

# 👤 Patients

The Patients section provides information about registered patients.

Patient information can include:

* Patient name
* Age
* Medical condition

### Patients Screenshot

![Patients](screenshots/patients.png)

---

# 📅 Appointment Management

The appointment module allows users to create and view appointments.

Appointment information includes:

* Patient name
* Doctor
* Appointment date
* Appointment time

Appointments are stored in a **SQLite database**.

### Appointments Screenshot

![Appointments](screenshots/appointments.png)

---

# 🤖 AI Disease Prediction

The system includes a machine-learning-based disease prediction feature.

Users can enter/select symptoms such as:

* 🌡️ Fever
* 😷 Cough
* 🤕 Headache
* 😴 Fatigue

The trained machine-learning model processes the symptoms and returns a predicted disease.

### AI Prediction Screenshot

![AI Disease Prediction](screenshots/prediction.png)

> ⚠️ **Medical Disclaimer:** This AI prediction feature is developed for educational and demonstration purposes only. It is not a medical diagnostic tool and should not replace advice from a qualified healthcare professional.

---

# 🧠 Machine Learning

The machine-learning component uses a dataset containing symptoms and disease information.

The trained model is stored using Joblib.

```text
model/
├── disease_model.pkl
├── label_encoder.pkl
└── train_model.py
```

### Machine Learning Workflow

```text
Symptoms Dataset
       ↓
Data Preparation
       ↓
Model Training
       ↓
Trained ML Model
       ↓
Flask Application
       ↓
User Symptoms
       ↓
Disease Prediction
```

---

# 🛠️ Technologies Used

| Technology      | Purpose                         |
| --------------- | ------------------------------- |
| 🐍 Python       | Backend development             |
| 🌐 Flask        | Web framework                   |
| 🗄️ SQLite      | Database                        |
| 🧠 Scikit-learn | Machine learning                |
| 📦 Joblib       | Model loading and serialization |
| 📄 HTML5        | Web page structure              |
| 🎨 CSS3         | User interface                  |
| 📊 CSV          | Dataset                         |
| 🔧 Git          | Version control                 |
| 🐙 GitHub       | Source code hosting             |

---

# 📁 Project Structure

```text
ai-hospital-management-system/
│
├── app.py
├── README.md
├── requirements.txt
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
├── screenshots/
│   ├── dashboard.png
│   ├── doctors.png
│   ├── patients.png
│   ├── appointments.png
│   └── prediction.png
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

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/munnakalyani/ai-hospital-management-system.git
```

## 2. Navigate to the Project

```bash
cd ai-hospital-management-system
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

The application will normally run at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser.

---

# 🗄️ Database

The application uses **SQLite** to store appointment information.

The database contains an appointments table with fields such as:

```text
id
patient_name
doctor
appointment_date
appointment_time
```

The local database file is excluded from Git using `.gitignore`.

---

# 📊 Dataset

The machine-learning dataset is located at:

```text
dataset/symptoms.csv
```

The dataset is used by the model-training process to build the disease prediction model.

---

# 🔐 Security & Privacy

This project is intended for educational and portfolio purposes.

A production hospital management system would require additional security measures, including:

* Secure authentication
* Password hashing
* Role-based access control
* Input validation
* HTTPS
* Database security
* Encryption of sensitive data
* Audit logging
* Secure session management
* Healthcare privacy compliance

**Do not upload real patient information to this public repository.**

---

# 🚀 Future Improvements

Planned improvements could include:

* 🔐 Doctor and patient authentication
* 👥 Role-based access control
* 📝 Patient medical history
* 💊 Prescription management
* 🧪 Laboratory reports
* 💳 Billing management
* 📧 Appointment notifications
* 📱 Mobile-responsive design
* 📈 Hospital analytics
* ☁️ Cloud deployment
* 🗃️ PostgreSQL/MySQL support
* 🧠 Improved machine-learning models
* 🔒 Enhanced security and privacy

---

# 🎯 Project Objectives

This project demonstrates practical experience with:

* Python programming
* Flask web development
* SQLite database integration
* Machine-learning integration
* HTML/CSS development
* Appointment management
* Model serialization
* Git and GitHub
* Project organization

---

# 👩‍💻 Author

### munnakalyani

GitHub:
https://github.com/munnakalyani

Project Repository:
https://github.com/munnakalyani/ai-hospital-management-system

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📸 Screenshots Gallery

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
