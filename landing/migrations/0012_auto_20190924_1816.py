# Generated by Django 2.2.5 on 2019-09-24 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20190924_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arg_vilao',
            name='universo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Universo'),
        ),
        migrations.AlterField(
            model_name='heroi',
            name='universo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Universo'),
        ),
    ]
