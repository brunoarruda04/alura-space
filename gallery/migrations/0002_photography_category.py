# Generated by Django 4.1.5 on 2023-01-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='category',
            field=models.CharField(choices=[('NEBULA', 'Nebula'), ('STAR', 'Star'), ('GALAXY', 'Galaxy'), ('PLANET', 'Planet')], default='', max_length=50),
        ),
    ]
