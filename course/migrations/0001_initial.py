# Generated by Django 2.2.5 on 2019-09-07 11:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('currency_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('currency_value', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': "Course's",
            },
        ),
    ]
