from django.test import TestCase

from .models import Lesson
# Create your tests here.

class LessonModelTests(TestCase):

	def test_longer_than_150_character_lesson_name_fails(self):
		test_lesson = Lesson(lesson_name="I am a really really really long lesson name, probably too long, so long it has become a ridiculous situation", description="desc", order=80)
		self.assertIs(test_lesson, False)
