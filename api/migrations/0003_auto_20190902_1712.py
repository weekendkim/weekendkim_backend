# Generated by Django 2.2.4 on 2019-09-02 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190902_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='writer_id',
        ),
    ]
