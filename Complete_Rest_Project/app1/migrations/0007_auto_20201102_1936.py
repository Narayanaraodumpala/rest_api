# Generated by Django 3.0 on 2020-11-02 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20201102_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carspacemodel',
            name='plan',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Carplan'),
        ),
        migrations.AlterField(
            model_name='carspacemodel',
            name='tyres',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.TyreModel'),
        ),
    ]