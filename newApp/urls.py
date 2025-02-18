from django.urls import path
from . import views

urlpatterns = [
    path('', views.newDisplay, name='newDisplay'),  # Root URL mapped to the newDisplay view
]
