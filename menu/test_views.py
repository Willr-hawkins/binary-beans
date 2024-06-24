from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Menu, EventMenus

class TestMenuViews(TestCase):

    def setUp(self):
        """
        Create the menus
        """
        self.menu_content = Menu(
            title='Test Menu', content='This is a test menu'
        )
        self.menu_content.save()
        self.eventMenu_content = EventMenus(
            title='Test Event Menu', content='This is a test event menu'
        )
        self.eventMenu_content.save()

    def test_render_menu_page(self):
        """
        Verifies get request for menu page.
        """
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Menu', response.content)
        self.assertIn(b'Test Event Menu', response.content)
