# src/main/base/urls.py
# Django modules
from django.urls import path
from .views import TaskDetail, Tasks, CreateTask, EditTask, DeleteTask, Login, RegistrationPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Tasks.as_view(), name='tasks'),
    path('login/>', Login.as_view(), name='login'),
    path('register/>', RegistrationPage.as_view(), name='register'),
    path('logout/>', LogoutView.as_view(next_page='login'), name='logout'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit-task/<int:pk>', EditTask.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task'),
]
