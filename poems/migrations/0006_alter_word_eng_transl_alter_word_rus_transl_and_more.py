# Generated by Django 5.0.6 on 2024-07-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0005_rename_text_poem_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='eng_transl',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='word',
            name='rus_transl',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]