# Generated by Django 3.2.12 on 2022-02-21 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0006_remove_student_removed_from_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='correct_cookies',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='finished_playing_at',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='started_playing_at',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
