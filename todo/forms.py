from django import forms
from todo.models import TaskModel

class TasksForm(forms.ModelForm):
  class Meta:
    model=TaskModel
    fields=['taskTitle','taskDescription']
 