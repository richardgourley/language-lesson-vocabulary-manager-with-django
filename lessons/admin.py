from django.contrib import admin
from .models import Lesson, Entry

# Register your models here.
class EntryInLine(admin.StackedInline):
	model = Entry

class LessonAdmin(admin.ModelAdmin):
	fieldsets = [
        (None, {'fields':['lesson_name','description','order']})
	]
	inlines = [EntryInLine]

admin.site.register(Lesson, LessonAdmin)
