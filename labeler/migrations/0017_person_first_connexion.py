# Generated by Django 4.2.2 on 2023-06-30 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0016_person_good_answers_person_total_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='first_connexion',
            field=models.BooleanField(default=True),
        ),
    ]
