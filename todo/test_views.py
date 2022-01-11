from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'todo/todo_list.html')

    # def test_get_add_item_page(self):

    # def test_get_edit_item_page(self):

    # def test_can_edit_item(self):

    # def test_can_delete_item(self):

    # def test_can_toggle_item(self):