# Generated by Django 4.2.2 on 2023-06-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0004_alter_person_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
