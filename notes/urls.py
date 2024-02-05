from django.urls import path
from .views import NoteListCreateAPIView, NoteDetailAPIView, TagListAPIView

urlpatterns = [
    path("", NoteListCreateAPIView.as_view(), name="note-list-create"),
    path("<int:pk>", NoteDetailAPIView.as_view(), name="note-detail"),
    path("tags", TagListAPIView.as_view(), name="tag-list"),
]
