# Generated by Django 4.2.3 on 2023-07-26 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0005_alter_livros_data_emprestimo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(default=datetime.date(2023, 7, 26)),
        ),
    ]
