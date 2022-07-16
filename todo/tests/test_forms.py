from django.test import TestCase
from todo .forms import *

class TestForms(TestCase):


    def test_create_todo_form(self):
        form = TodoForm(data={
        'title':'test title',
        'description':'test description',
        'status':True,
        })

        self.assertTrue(form.is_valid())
