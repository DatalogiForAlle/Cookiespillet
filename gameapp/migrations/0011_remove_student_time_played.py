# Generated by Django 3.2.12 on 2022-02-22 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0010_auto_20220222_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='time_played',
        ),
    ]
