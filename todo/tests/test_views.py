from django.test import TestCase
from todo.models import *
from django.urls import reverse

class TestTodoViews(TestCase):
    def test_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_list_detail(self):
        todo = Todo.objects.create(title="best todo", description="testing all")
        response = self.client.get(reverse('list_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        todo = todo = Todo.objects.create(title="best todo", description="testing all")
        response = self.client.get(reverse('delete_todo', args=[1]))

    def test_create_todo(self):
        data = {
        "title":"create todo",
        "description":"created description",
        "status":True
        }
        response = self.client.get(reverse('create_todo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')
        self.assertContains(response, 'title')
        self.assertContains(response, 'description')
        confirm_response = self.client.post(reverse("create_todo"), data=data)
        self.assertRedirects(confirm_response, reverse("list"))

    def test_update_todo(self):
        todo = Todo.objects.create(title="updated title")
        data = {
        "title":"update title",
        "description": "update description",
        "status":True
        }
        url = self.client.get(reverse('update_todo', args=[1]))
        self.assertTemplateUsed(url, 'update.html')
        response = self.client.post(reverse('update_todo', args=[1]), data=data)
        self.assertRedirects(response, reverse('list'))
        self.assertEqual(response.status_code, 302)
