# Generated by Django 4.2.2 on 2023-12-03 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('prof', models.CharField(max_length=60)),
                ('sala_num', models.IntegerField(max_length=3)),
            ],
        ),
    ]