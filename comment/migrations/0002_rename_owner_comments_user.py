# Generated by Django 4.2 on 2023-04-13 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='owner',
            new_name='user',
        ),
    ]
