# Generated by Django 3.2 on 2021-05-20 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0026_alter_members_last_name_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='student_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
