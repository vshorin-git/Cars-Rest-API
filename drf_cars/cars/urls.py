from django.urls import path
from . import views


app_name = 'car'
urlpatterns = [
    path('car/create', views.CarCreateView.as_view()),
]
