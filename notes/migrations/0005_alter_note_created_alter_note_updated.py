# Generated by Django 5.0.1 on 2024-02-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_note_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
