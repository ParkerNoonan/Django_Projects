# Generated by Django 3.1.3 on 2021-01-08 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Act_model_num', models.CharField(max_length=15)),
                ('Act_pressure', models.IntegerField()),
                ('Act_OST', models.IntegerField()),
                ('Act_OMT', models.IntegerField()),
                ('Act_OET', models.IntegerField()),
                ('Act_IST', models.IntegerField()),
                ('Act_IMT', models.IntegerField()),
                ('Act_IET', models.IntegerField()),
            ],
        ),
    ]
