# Generated by Django 4.1.4 on 2022-12-14 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recommend',
        ),
    ]
