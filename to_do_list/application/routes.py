from flask import render_template, redirect, url_for

from application import app, db
from application.models import Tasks

@app.route('/')
def home():
    task_list = Tasks.query.all()
    return render_template('layout.html', task_list=task_list)

@app.route('/add/<task>')
def add(task):
    new_task = Tasks(task=task)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    complete_task = Tasks.query.get(task_id)
    complete_task.is_complete = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/incomplete/<int:task_id>')
def incomplete(task_id):
    incomplete_task = Tasks.query.get(task_id)
    incomplete_task.is_complete = False
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<task>')
def update(task):
    first_task = Tasks.query.first()
    first_task.task = task
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete = Tasks.query.get(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
