# Generated by Django 4.1 on 2023-04-15 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0005_rename_id_usuarios_partidas_id_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='partidas',
            name='nivel',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
