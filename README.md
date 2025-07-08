# 📝 Flask To-Do App with Login

A simple, clean **To-Do List app** built with **Flask** and **Tailwind CSS**, featuring user registration and login functionality.

---

## ⚙️ Features

- ✅ User Registration & Login (Flask-Login)
- 🧠 Each user has their own private to-do list
- ➕ Add, ✅ mark complete, and ❌ delete tasks
- 🎨 Responsive Tailwind CSS styling
- 🗃️ SQLite database with SQLAlchemy ORM

---

## 📂 Project Structure

```
flask_todo_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       └── register.html
├── static/
├── run.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/AhrimanXD/flask-todo-app.git
cd flask-todo-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 5. Run the app

```bash
flask run
```

---

## 🧪 Default Config

The app uses **SQLite** and has a basic config setup in `config.py`. You can change the `SECRET_KEY` and `SQLALCHEMY_DATABASE_URI` if needed.

---

## 🎨 Tailwind CSS

Tailwind is included via CDN in `base.html`. No additional setup required.

---

## 📄 License

MIT License. Free to use, modify, or share.

---

## 🙋‍♂️ Author

Built by [AhrimanXD](https://github.com/AhrimanXD).  
Check out the full tutorial on [YouTube](https://www.youtube.com/@N_e_o_x_d) — coming soon!