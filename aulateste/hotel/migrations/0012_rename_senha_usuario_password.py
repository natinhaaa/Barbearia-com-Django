# Generated by Django 5.0.5 on 2024-05-21 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_alter_reserva_data_alter_reserva_nome_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='senha',
            new_name='password',
        ),
    ]
