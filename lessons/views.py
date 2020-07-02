from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from django.db.models import Count

from .models import Lesson, Entry
from .forms import SearchEntryForm

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'lessons/index.html'

# 10 lessons with lowest order number 
class FeaturedLessonsView(generic.ListView):
    template_name = 'lessons/featured.html'
    context_object_name = 'featured_lessons'

    def get_queryset(self):
        return Lesson.objects.annotate(num_entries=Count('entry')).filter(num_entries__gt=0).order_by('order')[:10]


class AllLessonsView(generic.ListView):
    template_name = 'lessons/all.html'
    context_object_name = 'all_lessons'

    def get_queryset(self):
        return Lesson.objects.annotate(num_entries=Count('entry')).filter(num_entries__gt=0)

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

class DisplayView(generic.DetailView):
    model = Lesson
    template_name = 'lessons/display.html'

    def get_queryset(self):
        return Lesson.objects.annotate(num_entries=Count('entry')).filter(num_entries__gt=0)
