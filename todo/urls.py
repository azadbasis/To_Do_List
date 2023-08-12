from django.urls import path
from . import views
urlpatterns = [

    path('', views.HomeView.as_view(), name='home'), 

    path('add_tasks/', views.AddTasksView.as_view(), name='addtasks'),
 
    path('show_tasks/', views.ShowTasksView.as_view(), name='showtasks'),
    
    path('edit_tasks/<int:pk>', views.EditTasksView.as_view(), name='edittasks'),

    path('delete_books/<int:pk>', views.DeleteTaskView.as_view(), name='deletetaks'),
    
    path('mark-completed/<int:task_id>', views.MarkTaskCompletedView.as_view(), name='mark_completed'),
    
    path('completed-tasks/', views.ShowCompletedTasksView.as_view(), name='completed_tasks'),
     
]