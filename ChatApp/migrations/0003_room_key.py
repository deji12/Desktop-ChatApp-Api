# Generated by Django 4.1.5 on 2023-01-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0002_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
