# Generated by Django 2.1.7 on 2019-02-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=128, unique=True)),
                ('sn', models.CharField(max_length=128, unique=True)),
                ('aktiven', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('som_id', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]
