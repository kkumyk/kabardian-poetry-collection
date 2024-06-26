# Generated by Django 5.0.6 on 2024-05-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(max_length=100)),
                ('eng_transl', models.CharField(max_length=100)),
                ('rus_transl', models.CharField(max_length=100)),
                ('ipa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('words', models.ManyToManyField(to='poems.word')),
            ],
        ),
    ]
