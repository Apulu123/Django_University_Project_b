# Generated by Django 4.1.10 on 2023-10-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w2', '0003_armmetrics_footmetrics_gamerecord_handmetrics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerecord',
            name='ID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gamerecord',
            name='UID',
            field=models.IntegerField(),
        ),
    ]
