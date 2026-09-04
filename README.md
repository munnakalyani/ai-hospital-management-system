# 🏥 AI Hospital Management System

<p align="center">

### 🤖 Smart Hospital Management with AI-Powered Disease Prediction

A web-based hospital management application built using **Python, Flask, SQLite, HTML, CSS, and Machine Learning**.

</p>

---

## 🌐 Live Demo

🚀 **Live Application:** Coming Soon

> The application will be deployed online so users can access the hospital management system from any device.

### 💻 Run Locally

After starting the Flask application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

### 🔗 Application Pages

| Page             | Description                       | Link                                                    |
| ---------------- | --------------------------------- | ------------------------------------------------------- |
| 🏠 Home          | Main hospital page                | [Open Home](http://127.0.0.1:5000/)                     |
| 📊 Dashboard     | Hospital administration dashboard | [Open Dashboard](http://127.0.0.1:5000/dashboard)       |
| 👨‍⚕️ Doctors    | Doctor information                | [Open Doctors](http://127.0.0.1:5000/doctors)           |
| 👤 Patients      | Patient information               | [Open Patients](http://127.0.0.1:5000/patients)         |
| 📅 Appointments  | Appointment management            | [Open Appointments](http://127.0.0.1:5000/appointments) |
| 🤖 AI Prediction | Disease prediction                | [Open AI Prediction](http://127.0.0.1:5000/prediction)  |

> ⚠️ These `127.0.0.1` links work only on the computer where the Flask server is running. Replace them with your deployed URL when the application is hosted online.

---

# 📌 About the Project

The **AI Hospital Management System** is a full-stack web application designed to simplify common hospital administration tasks.

The project combines hospital management functionality with an **AI-based disease prediction module**.

The system allows users to:

* 📊 View a hospital dashboard
* 👨‍⚕️ View doctors
* 👤 View patients
* 📅 Create and view appointments
* 🤖 Predict possible diseases from symptoms
* 🗄️ Store appointment information using SQLite

This project demonstrates the integration of **web development, databases, and machine learning** into a single application.

---

# ✨ Key Features

## 📊 1. Hospital Dashboard

The dashboard provides a centralized view of hospital information.

### Dashboard includes:

* 👨‍⚕️ Doctor count
* 👤 Patient count
* 📅 Appointment count
* 📋 Recent appointments
* 🔗 Navigation to hospital services

### Dashboard

![Hospital Dashboard](screenshots/dashboard.png)

---

## 👨‍⚕️ 2. Doctor Management

The Doctors page displays information about hospital doctors.

Information can include:

* Doctor name
* Specialization
* Years of experience

### Doctors

![Doctors](screenshots/doctors.png)

---

## 👤 3. Patient Management

The Patients page displays patient information.

Information can include:

* Patient name
* Age
* Medical condition

### Patients

![Patients](screenshots/patients.png)

---

## 📅 4. Appointment Management

The appointment system allows users to create and view appointments.

Each appointment contains:

* Patient name
* Doctor
* Appointment date
* Appointment time

Appointments are stored in a **SQLite database**.

### Appointments

![Appointments](screenshots/appointments.png)

---

## 🤖 5. AI Disease Prediction

The application contains a machine-learning module for disease prediction.

Users can provide symptoms such as:

* 🌡️ Fever
* 😷 Cough
* 🤕 Headache
* 😴 Fatigue

The trained machine-learning model processes the symptoms and returns a predicted disease.

### AI Disease Prediction

![AI Disease Prediction](screenshots/prediction.png)

> ⚠️ **Medical Disclaimer:** This feature is for educational and demonstration purposes only. It is not intended to provide medical diagnosis or replace professional medical advice.

---

# 🧠 Machine Learning

The disease prediction component uses a trained machine-learning model.

### Model files

```text
model/
├── disease_model.pkl
├── label_encoder.pkl
└── train_model.py
```

### Dataset

The dataset is stored in:

```text
dataset/
└── symptoms.csv
```

### Prediction Workflow

```text
             Symptoms
                 │
                 ▼
        ┌─────────────────┐
        │   User Input    │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Machine Learning│
        │     Model       │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Disease Result  │
        └─────────────────┘
```

---

# 🛠️ Technologies Used

| Technology      | Purpose                     |
| --------------- | --------------------------- |
| 🐍 Python       | Backend programming         |
| 🌐 Flask        | Web application framework   |
| 🗄️ SQLite      | Database                    |
| 🧠 Scikit-learn | Machine learning            |
| 📦 Joblib       | Model serialization/loading |
| 📄 HTML5        | Frontend structure          |
| 🎨 CSS3         | Styling                     |
| 📊 CSV          | Dataset                     |
| 🔧 Git          | Version control             |
| 🐙 GitHub       | Source code hosting         |

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

## 2. Enter the Project

```bash
cd ai-hospital-management-system
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

## 4. Activate the Environment

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

The application will run at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser.

---

# 🗄️ Database

The application uses **SQLite** for appointment management.

The appointments table contains:

```text
id
patient_name
doctor
appointment_date
appointment_time
```

The local database file is excluded from Git using `.gitignore`.

---

# 📸 Screenshots

## 📊 Dashboard

![Dashboard](screenshots/dashboard.png)

## 👨‍⚕️ Doctors

![Doctors](screenshots/doctors.png)

## 👤 Patients

![Patients](screenshots/patients.png)

## 📅 Appointments

![Appointments](screenshots/appointments.png)

## 🤖 AI Disease Prediction

![AI Disease Prediction](screenshots/prediction.png)

---

# 🔐 Security & Privacy

This project is intended for educational and portfolio purposes.

For a production hospital system, additional security would be required, including:

* Secure authentication
* Password hashing
* Role-based access control
* Input validation
* HTTPS
* Encryption of sensitive information
* Secure database configuration
* Audit logging
* Healthcare privacy compliance

**Do not use real patient information in this public repository.**

---

# 🚀 Future Improvements

Possible future enhancements include:

* 🔐 Doctor and patient login
* 👥 Role-based access control
* 📝 Patient medical history
* 💊 Prescription management
* 🧪 Laboratory reports
* 💳 Billing system
* 📧 Appointment notifications
* 📱 Mobile-responsive interface
* 📈 Hospital analytics
* ☁️ Cloud deployment
* 🗃️ PostgreSQL/MySQL support
* 🧠 Improved AI prediction models
* 🔒 Advanced security

---

# 🎯 Project Objectives

This project demonstrates practical experience in:

* Python
* Flask
* Machine Learning
* SQLite
* HTML/CSS
* Database integration
* Web application development
* Git
* GitHub
* Machine-learning model integration

---

# 👩‍💻 Author

## munnakalyani

GitHub:

https://github.com/munnakalyani

Repository:

https://github.com/munnakalyani/ai-hospital-management-system

---

# ⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.

---

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes**.

The AI disease prediction feature should not be used as a substitute for diagnosis, treatment, or advice from a qualified healthcare professional.

