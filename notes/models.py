from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "tag"


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    url = models.URLField(null=True)
    status = models.CharField(max_length=10, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        db_table = "note"
