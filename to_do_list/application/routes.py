from application import app, db
from application.models import Tasks

@app.route('/')
def read():
    task_list = Tasks.query.all()
    tasks_string = ""
    for task in task_list:
        if task.is_complete == True:
            task.task = task.task + "- COMPLETE"
        tasks_string += "<br>"+ task.task
    return tasks_string

@app.route('/add/<task>')
def add(task):
    new_task = Tasks(task=task, is_complete=False)
    db.session.add(new_task)
    db.session.commit()
    return "A new task has been added to the list"

@app.route('/complete/<int:task_id>')
def complete(task_id):
    complete_task = Tasks.query.get(task_id)
    complete_task.is_complete = True
    db.session.commit()
    return "Task with id " + str(task_id) + "has been completed"

@app.route('/incomplete/<int:task_id>')
def incomplete(task_id):
    incomplete_task = Tasks.query.get(task_id)
    incomplete_task.is_complete = False
    db.session.commit()
    return "Task with id " + str(task_id) + "is incomplete"

@app.route('/update/<task>')
def update(task):
    first_task = Tasks.query.first()
    first_task.task = task
    db.session.commit()
    return first_task.name

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete = Tasks.query.get(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return "Deleted task with id " + str(task_id)
