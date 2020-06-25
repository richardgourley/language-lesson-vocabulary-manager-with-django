from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Lesson, Entry
from .forms import SearchEntryForm

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
    if request.method == 'POST':
        form = SearchEntryForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            search_result = Entry.objects.filter(entry_text__icontains=request.POST['search_term']).order_by('entry_text')
            message = "We found 1 matching result" if len(search_result) == 1 else "We found {} matching results.".format(len(search_result))
            return render(request, 'lessons/searchentries.html', {'search_result':search_result, 'message':message, 'form':form})
    else:
        form = SearchEntryForm()
            
    return render(request, 'lessons/searchentries.html', {'search_result':'','message':'', 'form':form})

def display(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk = lesson_id)
    return render(request, 'lessons/display.html', {'lesson':lesson})






