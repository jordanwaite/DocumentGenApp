# Generated by Django 3.2 on 2021-08-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0046_auto_20210810_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='academic_history',
            field=models.CharField(default='academic_history', max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='aptitude',
            field=models.CharField(default='aptittude', max_length=4),
        ),
        migrations.AlterField(
            model_name='members',
            name='board_findings',
            field=models.CharField(default='board_findings', max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='board_rec',
            field=models.CharField(default='board_rec', max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='credits',
            field=models.CharField(default='credits', max_length=3),
        ),
        migrations.AlterField(
            model_name='members',
            name='disciplinary_history',
            field=models.CharField(default='disciplinary_history', max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='gpa',
            field=models.CharField(default='gpa', max_length=4),
        ),
        migrations.AlterField(
            model_name='members',
            name='major',
            field=models.CharField(default='major', max_length=50),
        ),
        migrations.AlterField(
            model_name='members',
            name='performance_history',
            field=models.CharField(default='performance_history', max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='present',
            field=models.CharField(choices=[('Yes', 'was'), ('No', 'was not')], default='was', max_length=10),
        ),
    ]
