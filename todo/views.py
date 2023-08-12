
from django.http import HttpResponse
from django.shortcuts import render,redirect
from todo.forms import TasksForm
from todo.models import TaskModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.views import View

# Create your views here.


class HomeView(TemplateView):
     template_name='home.html'
     
class AddTasksView(CreateView):
    model=TaskModel
    template_name='add_tasks.html'
    form_class=TasksForm  
    success_url=reverse_lazy('showtasks')  
     
# class ShowTasksView(ListView):
#     model=TaskModel
#     template_name='show_tasks.html'
#     context_object_name='data'

class ShowTasksView(ListView):
    model=TaskModel
    template_name='show_tasks.html'
    context_object_name='data'
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=False)

class EditTasksView(UpdateView):
    model=TaskModel
    template_name='add_tasks.html'
    form_class=TasksForm  
    success_url=reverse_lazy('showtasks') 

class DeleteTaskView(DeleteView):
     model=TaskModel
     template_name='delete_confirmation.html'
     success_url=reverse_lazy('showtasks')     

class MarkTaskCompletedView(View):
    def get(self, request, task_id, *args, **kwargs):
        task = TaskModel.objects.get(pk=task_id)
        task.is_completed = True
        task.save()
        return redirect('completed_tasks')  # Redirect to the completed_tasks view

class ShowCompletedTasksView(FormView):
    form_class = TasksForm
    template_name = 'completed_tasks.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TaskModel.objects.filter(is_completed=True)
        return context


 
   