from django.urls import path
from . import views

urlpatterns = [
    path('notes',views.NotesListView.as_view()),
    path('notes/<int:pk>',views.DetailListView.as_view()),
]
