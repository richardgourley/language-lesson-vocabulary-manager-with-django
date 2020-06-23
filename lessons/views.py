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

def search_entries(request):
    search_result = ''
    message = ''
    if request.POST:
        if request.POST['entry_search'] == '':
            message = 'Please enter a word or a sentence.'
        else:
            search_result = Entry.objects.filter(entry_text__icontains=request.POST['entry_search']).order_by('entry_text')
            message = "We found 1 matching result" if len(search_result) == 1 else "We found {} matching results.".format(len(search_result))
    context = {
        'search_result':search_result,
        'message':message
    }
    return render(request, 'lessons/searchentries.html', context)

def display(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk = lesson_id)
    return render(request, 'lessons/display.html', {'lesson':lesson})





