# Generated by Django 5.0.6 on 2024-05-13 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kabardian_poetry_api', '0005_vocabulary_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='kab_transl',
            new_name='rus_transl',
        ),
    ]