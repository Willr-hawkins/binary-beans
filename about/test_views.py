from django.urls import reverse
from django.test import TestCase
from .models import About

class TestAboutViews(TestCase):

    def setUp(self):
        """
        Creates About content
        """
        self.about_content = About(
            title='Test About', content='This is a test about'
        )
        self.about_content.save()

    def test_render_about_page(self):
        """
        Verifies get request for About page.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test About', response.content)