# Generated by Django 3.2 on 2021-08-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0047_auto_20210830_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='present',
            field=models.CharField(choices=[('Yes', 'was'), ('No', 'was not')], default='Yes', max_length=10),
        ),
    ]
