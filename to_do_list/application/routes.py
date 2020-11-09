from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Tasks
from application.forms import TaskForm, OrderForm

@app.route('/', methods=['GET','POST'])
def home():
    form = OrderForm()
    totals = {
            'number_completed':Tasks.query.filter_by(is_complete=True).count(),
            'total':Tasks.query.count()
            }
    if form.order.data == "new":
        task_list = Tasks.query.order_by(Tasks.id.desc()).all()
    elif form.order.data == "old":
        task_list = Tasks.query.order_by(Tasks.id).all()
    elif form.order.data == "completed":
        task_list = Tasks.query.order_by(Tasks.is_complete.desc()).all()
    elif form.order.data == "incompleted":
        task_list = Tasks.query.order_by(Tasks.is_complete).all()
    else:
        task_list = Tasks.query.all()
    return render_template('index.html', task_list=task_list, form=form, totals=totals)

@app.route('/add', methods=['GET','POST'])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Tasks(task=form.task.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

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

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    form = TaskForm()
    task_to_update = Tasks.query.get(task_id)
    if form.validate_on_submit():
        task_to_update.task = form.task.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.task.data = task_to_update.task
    return render_template('update.html', form=form)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete = Tasks.query.get(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
