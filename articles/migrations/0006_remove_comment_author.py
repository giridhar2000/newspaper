# Generated by Django 3.1.3 on 2020-11-17 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
