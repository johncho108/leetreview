# Generated by Django 3.2.7 on 2021-10-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20211015_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
