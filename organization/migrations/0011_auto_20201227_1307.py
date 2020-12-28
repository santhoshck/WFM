# Generated by Django 3.1.4 on 2020-12-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_auto_20201227_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalorgunit',
            name='org',
        ),
        migrations.RemoveField(
            model_name='orgunit',
            name='org',
        ),
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='time_percent',
            field=models.IntegerField(null=True, verbose_name='100 if Full Time'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='time_percent',
            field=models.IntegerField(null=True, verbose_name='100 if Full Time'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
