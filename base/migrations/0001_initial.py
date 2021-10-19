# Generated by Django 3.2.7 on 2021-10-01 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('user_code', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
