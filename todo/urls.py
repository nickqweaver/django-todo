from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:todo_id>/sick/', views.detail, name='sick'),

]
