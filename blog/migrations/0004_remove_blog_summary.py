# Generated by Django 3.0.3 on 2020-02-17 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200217_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='summary',
        ),
    ]
