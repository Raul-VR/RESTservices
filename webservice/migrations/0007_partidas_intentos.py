# Generated by Django 4.1 on 2023-04-15 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0006_partidas_nivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='partidas',
            name='intentos',
            field=models.IntegerField(default=0),
        ),
    ]