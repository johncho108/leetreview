# Generated by Django 3.2.7 on 2021-10-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20211012_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='optimized_code',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='user_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user_code',
            field=models.TextField(null=True),
        ),
    ]
