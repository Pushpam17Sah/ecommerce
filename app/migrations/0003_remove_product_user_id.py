# Generated by Django 4.1.7 on 2023-03-24 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_id',
        ),
    ]
