# Generated by Django 3.0 on 2020-11-02 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20201102_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carspacemodel',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Carplan'),
        ),
        migrations.AlterField(
            model_name='carspacemodel',
            name='tyres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.TyreModel'),
        ),
    ]
