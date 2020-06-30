from django.test import TestCase, Client
from django.urls import reverse

from .models import Lesson
# Create your tests here.

class LessonModelTests(TestCase):

    def test_lesson_with_order_default_returns_100(self):
        test_lesson = Lesson(lesson_name="name", description="description")
        self.assertIs((test_lesson.order == 100), True)

class LessonIndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status_lessons_index_page_is_200(self):
        response = self.client.get('/lessons/')
        self.assertIs(response.status_code, 200)


class LessonFeaturedLessonsViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status_featured_lessons_page_is_200(self):
        response = self.client.get(reverse('lessons:featured_lessons'))
        self.assertIs(response.status_code, 200)

    def test_featured_lessons_not_included_without_entries(self):
        '''
        Tests that lessons which have no entries attached to them do NOT appear in the 
        featured lessons list.
        '''
        Lesson.objects.create(lesson_name="lesson1", description="lesson1 description")
        Lesson.objects.create(lesson_name="lesson2", description="lesson2 description")
        response = self.client.get(reverse('lessons:featured_lessons'))
        self.assertQuerysetEqual(
            response.context['featured_lessons'],
            []
        )


class LessonAllLessonsViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status_all_lessons_page_is_200(self):
        response = self.client.get(reverse('lessons:all_lessons'))
        self.assertIs(response.status_code, 200)

    def test_all_lessons_not_included_without_entries(self):
        '''
        Tests that lessons which have no entries attached to them do NOT appear in the 
        all lessons list.
        '''
        Lesson.objects.create(lesson_name="lesson1", description="lesson1 description")
        Lesson.objects.create(lesson_name="lesson2", description="lesson2 description")
        response = self.client.get(reverse('lessons:all_lessons'))
        self.assertQuerysetEqual(
            response.context['all_lessons'],
            []
        )











