# Generated by Django 4.2.2 on 2023-12-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educaapp', '0002_comentarios_alter_materias_sala_num_conteudos'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='id_conteudo',
            field=models.IntegerField(default=0),
        ),
    ]
