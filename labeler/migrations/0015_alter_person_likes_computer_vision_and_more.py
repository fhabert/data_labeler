# Generated by Django 4.2.2 on 2023-06-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0014_alter_person_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='likes_computer_vision',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='likes_law',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='likes_real_estate',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
