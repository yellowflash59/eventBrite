# Generated by Django 3.1.7 on 2021-03-08 06:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0006_auto_20210308_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='is_liked',
            field=models.ManyToManyField(blank=True, related_name='events_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
