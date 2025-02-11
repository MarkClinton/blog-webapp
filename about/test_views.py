from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About

class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About(title="About Us", profile_image="placeholder", content="About content")
        self.about.save()

    def test_render_about_page(self):
        response = self.client.get(reverse(
            'about_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Us", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collab_submission(self):
        """Test for posting a comment on a post"""
        post_data = {
            'name': 'John Hayes',
            'email': 'jhayes@test.com',
            'message': 'Hello There.'
        }
        response = self.client.post(reverse(
            'about_detail'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request submitted!',
            response.content
        )
