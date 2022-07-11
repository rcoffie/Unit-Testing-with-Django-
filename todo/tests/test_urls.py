from django.test import TestCase
from todo.models import Todo
# Create your tests here.

class URLTests(TestCase):
    def test_test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_todo_page(self):
        response = self.client.get('/create-todo/')
        self.assertEqual(response.status_code, 200)

    # def test_todo_detail_page(self):
    #     response = self.client.get('/1/list-detail/')
    #     self.assertEqual(response.status_code, 200)
