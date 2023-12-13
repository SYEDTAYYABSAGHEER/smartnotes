from django.urls import path
from . import views

# function views routes

# urlpatterns = [
#     path('home', views.home),
#     path('authroized', views.authroized)
# ]



urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('authroized', views.AuthroizedView.as_view())
]