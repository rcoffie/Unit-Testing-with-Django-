from django.urls import path
from todo import views
urlpatterns = [
    path('', views.list,name='list'),
    path('list-detail/<str:id>/', views.list_detail,name='list_detail'),
    path('create-todo/',views.create_todo,name='create_todo'),
    path('update-todo/<int:id>/',views.update_todo, name='update_todo'),
    path('delete-todo/<int:id>/',views.delete_todo,name='delete_todo'),

]
