# Generated by Django 3.2.7 on 2021-10-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_entry_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='source',
            field=models.CharField(choices=[('ME', '1'), ('YOU', '2'), ('WE', '3')], max_length=200, null=True),
        ),
    ]