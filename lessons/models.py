from django.db import models

# Create your models here.
class Lesson(models.Model):
	lesson_name = models.CharField(max_length=150)
	description = models.TextField()
	order = models.IntegerField(default=100)

	def __str__(self):
		return self.lesson_name

class Entry(models.Model):
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	entry_text = models.CharField(max_length=250)
	translation = models.CharField(max_length=250)

	def __str__(self):
	    return self.entry_text
