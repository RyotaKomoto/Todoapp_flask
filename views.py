from forms import CreateForm,UpdateForm, DeleteForm
from flask import request, render_template, url_for, redirect
from models import db, Tasks
from app import app
import contextlib

@contextlib.contextmanager
def transaction(session):
  try:
    yield
    session.commit()
  except Exception as e:
    session.rolleback()
    raise e
  
@app.route('/')
@app.route('/task_list')
def task_list():
  tasks = Tasks.query.all()
  form = DeleteForm(request.form)
  return render_template('task_list.html',tasks=tasks, form=form)

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
  form = CreateForm(request.form)
  if request.method == 'POST' and form.validate():
    subject = form.subject.data
    deadline = form.deadline.data
    comment = form.comment.data
    new_task = Tasks(subject, deadline, comment)

    with transaction(db.session):
      db.session.add(new_task)
    
    return redirect(url_for('task_list'))
  return render_template('create_task.html', form=form)

@app.route('/update_task/<int:task_id>',methods=['GET', 'POST'])
def update_task(task_id):
  form = UpdateForm(request.form)
  task = Tasks.query.get(task_id)
  if request.method=='POST' and form.validate():
    id = form.id.data
    subject = form.subject.data
    deadline = form.deadline.data
    comment = form.comment.data
    update_task = Tasks(subject, deadline, comment)
    with transaction(db.session):
      db.session.delete(task)
      db.session.add(update_task)

    return redirect(url_for('task_list'))
  return render_template('update_task.html', form=form, task=task)

@app.route('/delete_task', methods=['GET', 'POST'])
def delete_task():
  form = DeleteForm(request.form)
  if request.method == 'POST' and form.validate():
    id = form.id.data
    task = Tasks.query.get(id)
    with transaction(db.session):
      db.session.delete(task)
    return redirect(url_for('task_list'))
  return redirect(url_for('task_list'))
  
if __name__ == '__main__':
  app.run(debug=True)
  

