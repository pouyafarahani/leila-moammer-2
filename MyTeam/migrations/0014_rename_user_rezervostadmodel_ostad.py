# Generated by Django 4.1.4 on 2022-12-25 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyTeam', '0013_alter_dateostadmodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rezervostadmodel',
            old_name='user',
            new_name='ostad',
        ),
    ]
