# Generated by Django 3.2.16 on 2022-11-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('value', models.FloatField()),
                ('rectime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-rectime',),
            },
        ),
    ]
