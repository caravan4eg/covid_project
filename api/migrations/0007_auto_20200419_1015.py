# Generated by Django 3.0.5 on 2020-04-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200419_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
