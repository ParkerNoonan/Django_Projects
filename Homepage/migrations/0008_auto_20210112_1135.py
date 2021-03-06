# Generated by Django 3.1.3 on 2021-01-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0007_torque_table_valve_run_torque'),
    ]

    operations = [
        migrations.AddField(
            model_name='valves',
            name='Valve_Break_Torque',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valves',
            name='Valve_Break_Torque_SF',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valves',
            name='Valve_MAST',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valves',
            name='Valve_Run_Torque',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valves',
            name='Valve_Run_Torque_SF',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valves',
            name='Valve_Setpoint_Pres1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valves',
            name='Valve_Setpoint_Pres2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='valves',
            name='Valve_SafetyFactor',
            field=models.DecimalField(decimal_places=1, default=1.5, max_digits=2),
        ),
    ]
