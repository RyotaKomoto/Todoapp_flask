from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)
Migrate(app, db)

class Tasks(db.Model):

  __tablename__ = 'tasks'

  id = db.Column(db.Integer,primary_key=True)
  subject = db.Column(db.Text)
  deadline = db.Column(db.Integer)
  comment = db.Column(db.Text)

  def __init__(self, subject, deadline, comment):
    self.subject = subject
    self.deadline = deadline
    self.comment = comment