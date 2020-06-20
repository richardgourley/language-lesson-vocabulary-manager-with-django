from django.urls import path
from . import views

app_name = 'lessons'
urlpatterns = [
    path('', views.index, name="index"),
    path('latest/', views.latest_lessons, name="latest_lessons")
]
