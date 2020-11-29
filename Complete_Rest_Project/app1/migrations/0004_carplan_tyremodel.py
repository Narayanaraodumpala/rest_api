# Generated by Django 3.0 on 2020-11-01 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_carspacemodel_car_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='TyreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tyre_number', models.PositiveIntegerField()),
                ('tyre_company', models.CharField(max_length=30)),
                ('tyre_brand', models.CharField(max_length=20)),
                ('tyre_cost', models.FloatField()),
                ('lifetime', models.CharField(max_length=20)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.CarspaceModel')),
            ],
        ),
        migrations.CreateModel(
            name='Carplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_id', models.IntegerField()),
                ('plan_name', models.CharField(max_length=30)),
                ('current_status', models.CharField(max_length=30)),
                ('plan_validity', models.PositiveIntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.CarspaceModel')),
            ],
        ),
    ]
