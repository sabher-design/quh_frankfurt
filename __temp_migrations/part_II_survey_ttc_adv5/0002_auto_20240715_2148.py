# Generated by Django 2.2.12 on 2024-07-15 19:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part_II_survey_ttc_adv5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='trust_institutions_city',
            field=otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Im Allgemeinen habe ich Vertrauen in städtische Behörden.'),
        ),
    ]
