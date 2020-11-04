from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from application.models import Tasks

class SameTaskCheck:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        task_list = Tasks.query.all()
        for task in task_list:
            if field.data == task.task:
                raise ValidationError(self.message)

class TaskForm(FlaskForm):
    task = StringField('Enter your task to do:',
                validators=[
                    DataRequired(),
                    SameTaskCheck(message='That task already exists')
                ]
            )
    submit = SubmitField('Add task to task list')
