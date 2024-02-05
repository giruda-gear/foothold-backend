# notes/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Note, Tag


class NoteAPITestCase(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(id=1, name="youtube")
        self.tag2 = Tag.objects.create(id=2, name="article")

        self.client = APIClient()

    def test_get_notes(self):
        response = self.client.get(reverse("note-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response)

    def test_create_note_api(self):
        note_data = {
            "title": "Test Note",
            "desc": "This is a test note.",
            "url": "https://youtu.be/0LNx4zdMGO0?si=A_jkG4gD3eDFFFVZ",
            "status": "0",
            "tags": [self.tag1.id, self.tag2.id],
        }

        response = self.client.post(
            reverse("note-list-create"), data=note_data, format="json"
        )

        # Check if the response status code is 201 (created) indicating success
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the note was created in the database
        self.assertTrue(Note.objects.filter(title="Test Note").exists())

        # Optionally, you can check the response data for additional verification
        created_note_data = response.json()
        print(created_note_data)

        self.assertEqual(created_note_data["title"], "Test Note")
        self.assertEqual(created_note_data["tags"], [self.tag1.id, self.tag2.id])
