# Generated by Django 4.2.2 on 2023-06-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0011_alter_person_rate_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
