# Generated by Django 4.2 on 2023-04-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='film',
            field=models.CharField(default=False, max_length=300),
        ),
    ]
