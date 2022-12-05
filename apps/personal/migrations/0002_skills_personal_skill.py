# Generated by Django 4.1.2 on 2022-11-06 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, verbose_name='Habilidades')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.AddField(
            model_name='personal',
            name='skill',
            field=models.ManyToManyField(to='personal.skills'),
        ),
    ]
