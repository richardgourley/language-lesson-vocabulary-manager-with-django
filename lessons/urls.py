from django.urls import path
from . import views
from .views import IndexView, FeaturedLessonsView, AllLessonsView

app_name = 'lessons'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('featured/', FeaturedLessonsView.as_view(), name="featured_lessons"),
    path('viewall/', AllLessonsView.as_view(), name="all_lessons"),
    path('searchentries/', views.search_entries, name="search_entries"),
    path('<int:lesson_id>/', views.display, name="display")
]
