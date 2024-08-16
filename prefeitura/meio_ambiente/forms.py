from django import forms

from .models import *

class Plantio_de_ArvoreForm(forms.ModelForm):
    class Meta:
        model = Plantio_de_Arvores
        fields ='__all__'
        labels = {
            'larg_compr_calcada' : 'Largura X Comprimento da Calçada',
            'observacoes' : 'Observações',
            'cep' : 'CEP',
            'bairro' : 'Bairro',
            'nome_rua' : 'Nome da Rua',
            'ponto_refer' : 'Ponto de Referência'
        }

class Poda_de_ArvoresForm(forms.ModelForm):
    class Meta:
        model = Poda_de_Arvores
        fields = '__all__'
        labels = {
            'rua' : 'Rua',
            'numero' : 'Número',
            'bairro' : 'Bairro',
            'estado' : 'Estado',
            'cidade' : 'Cidade',
            'cep' : 'CEP',
            'ponto_refer' : 'Ponto de Referência',
            'observacoes' : 'Observações',
            'telefone' : 'Telefone'
        }

class lancamento_de_agua_servidasForm(forms.ModelForm):
    model = lancamento_de_agua_servidas
    fields = '__all__'
    labels = {
        'cep_problema' : 'Insira o CEP do local do Problema *',
        'bairro_problema' : 'Insira o Bairro do Problema*',
        'rua_problema' : 'Insira a Rua do local do problema *',
        'ponto_refer' : 'Ponto de referência: *',
        'observacoes' : 'Observações'
    }

class lancamento_esgotoForm(forms.ModelForm):
    model = lancamento_esgoto
    fields = '__all__'
    labels = {
        'cep_problema' : 'Insira o CEP do local do Problema *',
        'bairro_problema' : 'Insira o Bairro do Problema*',
        'rua_problema' : 'Insira a Rua do local do problema *',
        'ponto_refer' : 'Ponto de referência: *',
        'observacoes' : 'Observações'
    }

class poluicao_sonoraForm(forms.ModelForm):
    model = poluicao_sonora
    fields = '__all__'
    labels = {
        'observacoes' : 'Observações',
        'cep_problema' : 'Insira o CEP do local do Problema *',
        'bairro_problema' : 'Insira o Bairro do Problema*',
        'rua_problema' : 'Insira a Rua do local do problema *',
        'ponto_refer' : 'Ponto de referência: *'
    }

class corte_irregular_arvoresForm(forms.ModelForm):
    model = corte_irregular_arvores
    fields = '__all__'
    labels = {
        'observacoes' : 'Observações',
        'cep_problema' : 'Insira o CEP do local do Problema *',
        'bairro_problema' : 'Insira o Bairro do Problema*',
        'rua_problema' : 'Insira a Rua do local do problema *',
        'ponto_refer' : 'Ponto de referência: *'
    }

class poluicao_atmosfericaForm(forms.ModelForm):
    model = poluicao_atmosferica
    fields = '__all__'
    labels = {
        'observacoes' : 'Observações',
        'cep_problema' : 'Insira o CEP do local do Problema *',
        'bairro_problema' : 'Insira o Bairro do Problema*',
        'rua_problema' : 'Insira a Rua do local do problema *',
        'ponto_refer' : 'Ponto de referência: *'
    }

class invasao_area_preservacao_permanenteForm(forms.ModelForm):
    model = invasao_area_preservacao_permanente
    fields = '__all__'
    labels = {
        'observacoes' : 'Observações',
        'cep_problema' : 'Insira o CEP do local do Problema *',
        'bairro_problema' : 'Insira o Bairro do Problema*',
        'rua_problema' : 'Insira a Rua do local do problema *',
        'ponto_refer' : 'Ponto de referência: *'
    }

            
        
        