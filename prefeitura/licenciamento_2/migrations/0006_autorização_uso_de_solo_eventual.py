# Generated by Django 5.1 on 2024-08-23 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenciamento_2", "0005_alter_sedrub_cpf_alter_sedrub_requerente"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autorização_Uso_de_Solo_Eventual",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Descricao", models.TextField(default="Conteúdo")),
                ("Requerente", models.TextField(default=None)),
                ("CPF", models.IntegerField(default=None)),
                ("Ligação_de_Água", models.BooleanField(default=False)),
                ("Ligação_de_Energia", models.BooleanField(default=False)),
                ("Endereco", models.TextField()),
            ],
        ),
    ]
