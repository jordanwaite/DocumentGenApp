# Generated by Django 3.1.7 on 2021-02-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0013_auto_20210223_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='senior_member',
            field=models.BooleanField(default=False, verbose_name='Is this the senior board member?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='student_member',
            field=models.BooleanField(default=False, verbose_name='Is this the student?'),
            preserve_default=False,
        ),
    ]
