# Generated by Django 5.0.1 on 2024-01-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_trainee_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='date_certified',
            field=models.DateField(blank=True, null=True),
        ),
    ]
