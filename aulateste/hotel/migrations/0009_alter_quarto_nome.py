# Generated by Django 5.0.5 on 2024-05-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_remove_hotel_logo_hotel_foto_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarto',
            name='nome',
            field=models.CharField(choices=[('SOLTEIRO CONFORTÁVEL', 'Solteiro Confortável'), ('SOLTEIRO COM VISTA', 'Solteiro com Vista'), ('SOLTEIRO ECONÔMICO', 'Solteiro Econômico'), ('CASAL LUXO', 'Casal Luxo'), ('SUÍTE ROMÂNTICA', 'Suíte Romântica'), ('CASAL STANDARD', 'Casal Standard'), ('SUPERIOR COM VISTA', 'Superior com Vista'), ('COMFORT CLÁSSICO', 'Comfort Clássico'), ('COMFORT DELUXE', 'Comfort Deluxe'), ('COMFORT EXECUTIVO', 'Comfort Executivo'), ('COMFORT FAMILIAR', 'Comfort Familiar'), ('SUÍTE LUXO EXECUTIVO', 'Suíte Luxo Executivo'), ('SUÍTE PRESIDENCIAL', 'Suíte Presidencial'), ('LUXO PREMIUM', 'Luxo Premium'), ('SUÍTE REAL', 'Suíte Real')], max_length=20),
        ),
    ]
