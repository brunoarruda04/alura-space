# Generated by Django 4.1.5 on 2023-01-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_photography_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
