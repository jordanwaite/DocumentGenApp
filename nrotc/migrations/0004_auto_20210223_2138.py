# Generated by Django 3.1.7 on 2021-02-23 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0003_auto_20210223_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todelname',
            name='letter_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todelname',
            name='prb_date',
            field=models.DateField(),
        ),
    ]
