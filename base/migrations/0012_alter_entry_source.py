# Generated by Django 3.2.7 on 2021-10-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_entry_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='source',
            field=models.CharField(choices=[('LC', 'LeetCode'), ('HR', 'HackerRank'), ('CW', 'Codewars'), ('CF', 'Codeforces'), ('CC', 'CodeChef'), ('O', 'Other')], max_length=200, null=True),
        ),
    ]
