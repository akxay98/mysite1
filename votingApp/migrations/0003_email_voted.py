# Generated by Django 5.0.4 on 2024-05-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingApp', '0002_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='voted',
            field=models.BooleanField(default=False),
        ),
    ]
