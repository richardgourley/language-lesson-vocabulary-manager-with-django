from django.test import TestCase, Client
from django.urls import reverse

from .models import Lesson
# Create your tests here.

class LessonModelTests(TestCase):

    def test_lesson_with_order_default_returns_100(self):
        test_lesson = Lesson(lesson_name="name", description="description")
        self.assertIs((test_lesson.order == 100), True)

    def test_mock_test(self):
        # Create lesson without any entries
        test_lesson = Lesson(lesson_name="test_lesson",description="description of test lesson")
        all_lessons = [1,2,3]
        self.assertIs((len(all_lessons) == 3), True)


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status_lessons_index_page_is_200(self):
        response = self.client.get(reverse('lessons:index'))
        self.assertIs(response.status_code, 200)
