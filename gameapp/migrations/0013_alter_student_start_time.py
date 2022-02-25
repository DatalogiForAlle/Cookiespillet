# Generated by Django 3.2.12 on 2022-02-22 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0012_remove_student_finish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]