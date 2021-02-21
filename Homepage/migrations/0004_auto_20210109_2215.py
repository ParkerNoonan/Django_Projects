# Generated by Django 3.1.3 on 2021-01-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0003_auto_20210107_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Torque_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Valve_size', models.IntegerField()),
                ('Min_Torque', models.IntegerField()),
                ('Torque_Cnst1', models.IntegerField()),
                ('Torque_Cnst2', models.IntegerField()),
                ('MAST', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='actuator',
            name='Act_Setpoint1',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='actuator',
            name='Act_Setpoint2',
            field=models.IntegerField(default=120),
        ),
    ]