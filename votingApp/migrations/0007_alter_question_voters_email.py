# Generated by Django 5.0.4 on 2024-05-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingApp', '0006_question_voters_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='voters_email',
            field=models.TextField(),
        ),
    ]