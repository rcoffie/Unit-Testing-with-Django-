from django.urls import path
from todo import views
urlpatterns = [
    path('', views.list,name='list'),
    path('<str:id>/list-detail/', views.list_detail,name='list_detail'),
    path('create-todo/',views.create_todo,name='create_todo'),
    path('<int:id>/update-todo/',views.update_todo, name='update_todo'),
    path('delete-todo/<int:id>/',views.delete_todo,name='delete_todo'),

]
