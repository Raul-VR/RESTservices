# Generated by Django 4.1 on 2023-04-01 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0004_rename_id_usuario_partidas_id_usuarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partidas',
            old_name='id_usuarios',
            new_name='id_usuario',
        ),
    ]
