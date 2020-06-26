from django.urls import path
from . import views

app_name = 'lessons'
urlpatterns = [
    path('', views.index, name="index"),
    path('latest/', views.latest_lessons, name="latest_lessons"),
    path('featured/', views.featured_lessons, name="featured_lessons"),
    path('viewall/', views.all_lessons, name="all_lessons"),
    path('searchentries/', views.search_entries, name="search_entries"),
    path('<int:lesson_id>/', views.display, name="display")
]
