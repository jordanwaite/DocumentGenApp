# Generated by Django 3.2 on 2021-05-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrotc', '0028_auto_20210520_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='rank_recorder',
            new_name='member1_rank',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='service_recorder',
            new_name='member1_service',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='rank_senior',
            new_name='member2_rank',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='service_senior',
            new_name='member2_service',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='rank_voting1',
            new_name='recorder_rank',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='service_voting1',
            new_name='recorder_service',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='rank_voting2',
            new_name='senior_rank',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='service_voting2',
            new_name='senior_service',
        ),
        migrations.RemoveField(
            model_name='members',
            name='first_name_recorder',
        ),
        migrations.RemoveField(
            model_name='members',
            name='first_name_senior',
        ),
        migrations.RemoveField(
            model_name='members',
            name='first_name_voting1',
        ),
        migrations.RemoveField(
            model_name='members',
            name='first_name_voting2',
        ),
        migrations.RemoveField(
            model_name='members',
            name='last_name_recorder',
        ),
        migrations.RemoveField(
            model_name='members',
            name='last_name_senior',
        ),
        migrations.RemoveField(
            model_name='members',
            name='last_name_voting1',
        ),
        migrations.RemoveField(
            model_name='members',
            name='last_name_voting2',
        ),
        migrations.RemoveField(
            model_name='members',
            name='middle_initial_recorder',
        ),
        migrations.RemoveField(
            model_name='members',
            name='middle_initial_senior',
        ),
        migrations.RemoveField(
            model_name='members',
            name='middle_initial_voting1',
        ),
        migrations.RemoveField(
            model_name='members',
            name='middle_initial_voting2',
        ),
        migrations.AddField(
            model_name='members',
            name='member1_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='members',
            name='member2_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='members',
            name='recorder_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='members',
            name='senior_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
