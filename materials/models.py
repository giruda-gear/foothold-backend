from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "category"


class Material(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "material"
