# Generated by Django 3.0.5 on 2020-04-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200428_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to='images', verbose_name='Poster'),
        ),
    ]