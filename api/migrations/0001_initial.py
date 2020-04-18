# Generated by Django 3.0.5 on 2020-04-18 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250)),
                ('rayon', models.CharField(max_length=250)),
                ('oblast', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Населенный пункт',
                'verbose_name_plural': 'Населенные пункты',
            },
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=250)),
                ('sick', models.IntegerField()),
                ('dead', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('tests_made', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('where_is_it', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Location')),
            ],
            options={
                'verbose_name': 'Факт',
                'verbose_name_plural': 'Факты',
            },
        ),
    ]
