from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Count

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

    def test_featured_lessons_has_featured_lessons_key_in_context(self):
        '''
        Tests that response.context contains a 'featured_lessons' key
        '''
        response = self.client.get(reverse('lessons:featured_lessons'))
        has_featured_lessons_key = False 
        if 'featured_lessons' in response.context:
            has_featured_lessons_key = True

        self.assertIs(has_featured_lessons_key, True)

    def test_featured_lessons_no_lessons_found_displays_message(self):
        '''
        Tests that the html returned contains 'no lessons found' if no lessons exist
        '''
        response = self.client.get(reverse('lessons:featured_lessons'))
        contains_message = 'No lessons found' in str(response.content)
        self.assertIs(contains_message, True)


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

    def test_all_lessons_has_all_lessons_key_in_context(self):
        '''
        Tests that response.context contains an 'all_lessons' key
        '''
        response = self.client.get(reverse('lessons:all_lessons'))
        has_all_lessons_key = False 
        if 'all_lessons' in response.context:
            has_all_lessons_key = True

        self.assertIs(has_all_lessons_key, True)

    def test_all_lessons_no_lessons_found_displays_message(self):
        '''
        Tests that the html returned contains 'no lessons found' if no lessons exist
        '''
        response = self.client.get(reverse('lessons:all_lessons'))
        contains_message = 'No lessons found' in str(response.content)
        self.assertIs(contains_message, True)


class LessonDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_lesson_detail_without_entries_returns_404(self):
        '''
        Test to see if a 404 page appears when a lessons/id page is visited if that
        lesson does NOT have entries attached.
        '''
        l = Lesson.objects.create(lesson_name="lesson1", description="lesson1 description")
        url = reverse('lessons:display', args=(l.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_lesson_detail_with_entries_returns_200(self):
        '''
        A 'lessons/id' for a lesson that has entries attached to it, should
        return status_code 200
        '''
        l = Lesson.objects.create(lesson_name="test_lesson", description="test lesson desc")
        l.entry_set.create(entry_text="shoe", translation="zapato")
        url = reverse('lessons:display', args=(l.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)




