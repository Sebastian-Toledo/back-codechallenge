# Generated by Django 4.1.2 on 2022-10-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userLessons', '0002_remove_user_lessons_lesson_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, to='userLessons.user'),
        ),
    ]