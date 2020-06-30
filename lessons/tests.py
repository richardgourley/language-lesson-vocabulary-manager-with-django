from django.test import TestCase

from .models import Lesson
# Create your tests here.

class LessonModelTests(TestCase):

	def test_lesson_with_order_default_returns_100(self):
		test_lesson = Lesson(lesson_name="name", description="description")
		self.assertIs((test_lesson.order == 100), True)
