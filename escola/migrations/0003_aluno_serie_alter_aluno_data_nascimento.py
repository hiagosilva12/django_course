# Generated by Django 4.1.3 on 2022-11-25 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_aluno_nome_responsavel_aluno_sobrenome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='serie',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(default='', max_length=8),
        ),
    ]
