# Generated by Django 3.2.7 on 2021-10-15 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_entry_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='title',
        ),
    ]