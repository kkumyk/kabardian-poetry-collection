# Generated by Django 5.0.6 on 2024-07-23 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0006_alter_word_eng_transl_alter_word_rus_transl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='ipa',
        ),
    ]