# Generated by Django 3.0 on 2020-10-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=30, null=True)),
                ('car_brand', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('production', models.IntegerField(null=True)),
                ('fuel', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]