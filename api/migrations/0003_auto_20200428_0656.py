# Generated by Django 3.0.5 on 2020-04-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200427_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img_2',
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Original'),
        ),
    ]