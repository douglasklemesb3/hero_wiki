# Generated by Django 2.2.5 on 2019-09-23 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20190923_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arg_vilao',
            name='universo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Universo'),
        ),
        migrations.RemoveField(
            model_name='habilidade',
            name='hab_heroi',
        ),
        migrations.AddField(
            model_name='habilidade',
            name='hab_heroi',
            field=models.ManyToManyField(related_name='Habilidade', to='landing.Heroi'),
        ),
        migrations.AlterField(
            model_name='heroi',
            name='universo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Universo'),
        ),
    ]