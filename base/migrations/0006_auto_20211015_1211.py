# Generated by Django 3.2.7 on 2021-10-15 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20211015_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='link',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
