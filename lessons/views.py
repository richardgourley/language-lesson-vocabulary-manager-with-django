from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Lesson

# Create your views here.
def index(request):
	return render(request, 'lessons/index.html', {})

def latest_lessons(request):
	latest_lessons = Lesson.objects.all()[:5]
	context = {
	    'latest_lessons':latest_lessons
	}
	return render(request, 'lessons/latest.html', context)
