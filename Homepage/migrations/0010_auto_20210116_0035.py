# Generated by Django 3.1.3 on 2021-01-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0009_auto_20210116_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valves',
            name='Valve_Project_num',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]