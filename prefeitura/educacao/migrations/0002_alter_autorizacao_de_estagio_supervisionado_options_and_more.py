
# Generated by Django 5.1 on 2024-08-19 18:13



from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("educacao", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="autorizacao_de_estagio_supervisionado",
            options={"verbose_name": "SEDEC - Autorização de Estágio Supervisionado"},
        ),
        migrations.AlterModelOptions(
            name="autorizacao_para_pesquisa_crei_escola",
            options={"verbose_name": "SEDEC - Autorização para Pesquisa CREI/Escola"},
        ),
        migrations.AlterModelOptions(
            name="furto_extravio_ou_perda_de_equipamentos",
            options={
                "verbose_name": "SEDEC - Furto, Extravio, ou Perda de Equipamentos"
            },
        ),
        migrations.AlterModelOptions(
            name="solicitacao_de_espaco_fisico_escola_crei",
            options={
                "verbose_name": "SEDEC - Solicitação de Espaço Físico - Escola/CREI"
            },
        ),
        migrations.AlterModelOptions(
            name="solicitacao_diversa",
            options={"verbose_name": "SEDEC - Solicitação Diversa"},
        ),
    ]
