# In our main url file for the project, we need to include the URL conf for 'lessons'

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lessons/', include('lessons.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
