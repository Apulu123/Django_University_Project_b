# Generated by Django 4.1.10 on 2023-10-04 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('w2', '0002_userpartsid_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Arm_UID', models.CharField(max_length=20)),
                ('USER_UID', models.CharField(max_length=20)),
                ('LastStage', models.CharField(max_length=20)),
                ('TotalPlayTime', models.FloatField(default=0)),
                ('TotalPlayCount', models.IntegerField(default=0)),
                ('PassCount', models.IntegerField(default=0)),
                ('TotalGetCoin', models.IntegerField(default=0)),
                ('LastRecordId', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FootMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Foot_UID', models.CharField(max_length=20)),
                ('USER_UID', models.CharField(max_length=20)),
                ('LastStage', models.CharField(max_length=20)),
                ('TotalPlayTime', models.FloatField(default=0)),
                ('TotalPlayCount', models.IntegerField(default=0)),
                ('PassCount', models.IntegerField(default=0)),
                ('TotalGetCoin', models.IntegerField(default=0)),
                ('LastRecordId', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GameRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(max_length=20)),
                ('USER_UID', models.CharField(max_length=20)),
                ('PlayDate', models.DateField()),
                ('PlayPart', models.CharField(max_length=20)),
                ('UID', models.IntegerField(max_length=20)),
                ('PlayStage', models.CharField(max_length=20)),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
                ('DurationTime', models.DurationField()),
                ('AddCoin', models.IntegerField(default=0)),
                ('ExerciseCount', models.IntegerField(default=0)),
                ('EstablishTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HandMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hand_UID', models.CharField(max_length=20)),
                ('USER_UID', models.CharField(max_length=20)),
                ('LastStage', models.CharField(max_length=20)),
                ('TotalPlayTime', models.FloatField(default=0)),
                ('TotalPlayCount', models.IntegerField(default=0)),
                ('PassCount', models.IntegerField(default=0)),
                ('TotalGetCoin', models.IntegerField(default=0)),
                ('LastRecordId', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LimbMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Limb_UID', models.CharField(max_length=20)),
                ('USER_UID', models.CharField(max_length=20)),
                ('LastStage', models.CharField(max_length=20)),
                ('TotalPlayTime', models.FloatField(default=0)),
                ('TotalPlayCount', models.IntegerField(default=0)),
                ('PassCount', models.IntegerField(default=0)),
                ('TotalGetCoin', models.IntegerField(default=0)),
                ('LastRecordId', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Arm_UID', models.CharField(max_length=20)),
                ('Foot_UID', models.CharField(max_length=20)),
                ('Limb_UID', models.CharField(max_length=20)),
                ('Hand_UID', models.CharField(max_length=20)),
                ('TotalCoin', models.IntegerField(default=0)),
                ('USER_UID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserPartsID',
        ),
    ]
