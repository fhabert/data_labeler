# Generated by Django 4.2.2 on 2023-06-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0002_alter_person_rate_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
