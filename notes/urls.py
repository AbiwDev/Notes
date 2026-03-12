from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.list_notes, name='notes_list'),
    path('add/', views.add_notes, name='add_notes'),
    path('edit/<int:id>/', views.edit_notes, name='edit_notes'),
    path('delete/<int:id>/', views.delete_notes, name='delete_notes'),
    path('detail/<int:id>/', views.detail, name='detail'),
]