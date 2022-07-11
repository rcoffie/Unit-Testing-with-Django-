from django.test import TestCase
from todo.models import Todo

class TestAppModels(TestCase):
    def test_model_str(self):
        title = Todo.objects.create(title="testing todo")
        description = Todo.objects.create(description="test description")
        self.assertEqual(str(title), "testing todo")
