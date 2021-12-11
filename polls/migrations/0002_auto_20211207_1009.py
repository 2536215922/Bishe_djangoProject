# Generated by Django 3.2.9 on 2021-12-07 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField(default=0)),
                ('patient_name', models.CharField(max_length=20)),
                ('patient_gender', models.SmallIntegerField(choices=[(0, '女'), (1, '男')])),
                ('patient_birthday', models.CharField(max_length=20)),
                ('patient_physician', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField(default=0)),
                ('deviceid', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
