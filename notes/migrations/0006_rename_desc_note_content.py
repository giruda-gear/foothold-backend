# Generated by Django 5.0.1 on 2024-02-05 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_note_created_alter_note_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='desc',
            new_name='content',
        ),
    ]
