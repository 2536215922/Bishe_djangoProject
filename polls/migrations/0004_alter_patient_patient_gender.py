# Generated by Django 3.2.9 on 2021-12-07 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20211207_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_gender',
            field=models.CharField(max_length=20),
        ),
    ]
