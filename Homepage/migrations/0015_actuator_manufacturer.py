# Generated by Django 3.1.3 on 2021-01-29 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0014_auto_20210123_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='Manufacturer',
            field=models.CharField(default='Bettis', max_length=50),
            preserve_default=False,
        ),
    ]