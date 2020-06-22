from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Lesson, Entry

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
	all_entries = Entry.objects.order_by('entry_text')
	context = {
	    'all_entries':all_entries
	}
	return render(request, 'lessons/entries.html', context)

def display(request, lesson_id):
	lesson = get_object_or_404(Lesson, pk = lesson_id)
	return render(request, 'lessons/display.html', {'lesson':lesson})



