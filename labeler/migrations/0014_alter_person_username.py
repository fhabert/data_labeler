# Generated by Django 4.2.2 on 2023-06-28 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0013_alter_person_options_alter_person_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(default='fake', max_length=30, unique=True),
        ),
    ]
