# Generated by Django 3.1.7 on 2021-03-01 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0019_auto_20210228_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='rank',
            field=models.CharField(choices=[('Midshipman', 'Midshipman'), ('Officer Candidate', 'Officer Candidate'), ('LT', 'LT'), ('LCDR', 'LCDR'), ('CDR', 'CDR'), ('CAPT', 'Captain (Navy)'), ('Capt', 'Captain (USMC)'), ('Maj', 'Major'), ('LtCol', 'LtCol'), ('Col', 'Col')], max_length=20),
        ),
    ]
