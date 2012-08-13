from django.test import TestCase
from django.test.client import RequestFactory


class PrivateViewsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_undecorated_view(self):
        response = self.client.get('/undecorated/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('accounts/login' in response['Location'])

    def test_decorated_view(self):
        response = self.client.get('/test-decorator/')
        self.assertEqual(response.status_code, 200)

    def test_undecorated_class_based_view(self):
        response = self.client.get('/test-undecorated-class-based-view/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('accounts/login' in response['Location'])

    def test_decorated_class_based_view(self):
        response = self.client.get('/test-decorated-class-based-view/')
        self.assertEqual(response.status_code, 200)

    def test_list_public_views(self):
        """View listed in settings.PUBLIC_VIEWS"""
        response = self.client.get('/test-public-views/')
        self.assertEqual(response.status_code, 200)

    def test_list_public_paths(self):
        """View listed in settings.PUBLIC_PATHS"""
        response = self.client.get('/test-public-paths/')
        self.assertEqual(response.status_code, 200)
