# Generated by Django 3.0.3 on 2020-03-16 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleDetail', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='articleCategory',
        ),
        migrations.DeleteModel(
            name='articleDetail',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]