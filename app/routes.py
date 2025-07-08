from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User, Task
from .forms import RegisterForm, LoginForm, TaskForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET','POST'])
@login_required
def index():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(content = form.content.data, user = current_user)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('main.index'))
    tasks = Task.query.filter_by(user_id = current_user.id).order_by(Task.date_created.desc()).all()
    return render_template('index.html', form = form, tasks=tasks)

@main.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user != current_user:
        return redirect(url_for('main.index'))
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/toggle/<int:task_id>')
@login_required
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user != current_user:
        return redirect(url_for('main.index'))

    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered", 'error')
            return redirect(url_for('main.register'))
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            username = form.username.data,
            email = form.email.data,
            password = hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form = form)

@main.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.login'))