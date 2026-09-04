
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
