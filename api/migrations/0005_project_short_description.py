# Generated by Django 3.0.5 on 2020-04-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200423_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
