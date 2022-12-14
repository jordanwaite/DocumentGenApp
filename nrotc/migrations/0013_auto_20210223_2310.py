# Generated by Django 3.1.7 on 2021-02-23 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0012_auto_20210223_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='rank',
            field=models.CharField(choices=[('Midshipman', 'Midshipman'), ('Officer Candidate', 'Officer Candidate'), ('LT', 'LT'), ('LCDR', 'LCDR'), ('CDR', 'CDR'), ('CAPT', 'Captain (Navy)'), ('Capt', 'Captain (USMC)'), ('Maj', 'Major'), ('LtCol', 'LtCol'), ('Col', 'Col')], default='Midshipman', max_length=20),
        ),
    ]
