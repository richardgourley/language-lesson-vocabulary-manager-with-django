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

def all_lessons(request):
	all_lessons = Lesson.objects.all()
	context = {
	    'all_lessons':all_lessons
	}
	return render(request, 'lessons/all.html', context)

def individual_entries(request):
	all_lessons = Lesson.objects.all()
	context = {
	    'all_lessons':all_lessons
	}
	return render(request, 'lessons/entries.html', context)

def display(request, lesson_id):
	lesson = get_object_or_404(Lesson, pk = lesson_id)
	context = {
	    'lesson':lesson,
	}
	return render(request, 'lessons/display.html', {'lesson':lesson})

