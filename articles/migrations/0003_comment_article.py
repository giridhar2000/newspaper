# Generated by Django 3.1.3 on 2020-11-17 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
            preserve_default=False,
        ),
    ]
