from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(64), unique = True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable = False)

  tasks = db.relationship('Task', backref='user', lazy=True)

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(250), nullable=False)
  completed = db.Column(db.Boolean, default=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)