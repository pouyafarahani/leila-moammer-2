# Generated by Django 4.1.4 on 2023-01-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyTeam', '0020_myteammodel_price5'),
    ]

    operations = [
        migrations.AddField(
            model_name='userostadmodel',
            name='price5',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userostadmodel',
            name='price6',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userostadmodel',
            name='price7',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
