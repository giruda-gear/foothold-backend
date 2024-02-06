from rest_framework import generics

from notes.serializers import NoteDetailSerializer, NoteSerializer, TagSerializer
from notes.models import Note, Tag


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.prefetch_related("tags")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NoteDetailSerializer
        return NoteSerializer
