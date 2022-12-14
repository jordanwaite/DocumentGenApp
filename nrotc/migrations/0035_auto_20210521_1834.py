# Generated by Django 3.2 on 2021-05-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0034_alter_members_letter_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='prb_date',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='members',
            name='prb_location',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='members',
            name='prb_time',
            field=models.IntegerField(default=1230),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='student_on_LOA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='members',
            name='student_uniform',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='members',
            name='trigger',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='members',
            name='unit_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='PRBInfo',
        ),
    ]
