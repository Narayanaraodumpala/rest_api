# Generated by Django 3.0 on 2020-10-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20201024_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='carspacemodel',
            name='car_number',
            field=models.IntegerField(null=True),
        ),
    ]
