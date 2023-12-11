from django.forms import ModelForm
from django import forms
import educaapp.models as Models

class FormMaterias(ModelForm):
    nome = forms.CharField(label='nome', widget=forms.TextInput(attrs={'placeholder': 'Nome da matéria..'}))
    prof = forms.CharField(label='prof', widget=forms.TextInput(attrs={'placeholder': 'Nome do professor..'}))
    sala_num = forms.CharField(label='sala_num', widget=forms.NumberInput(attrs={'placeholder': 'Número da sala..'}))
    class Meta:
        model = Models.Materias
        fields = ['nome', 'prof','sala_num']

class FormConteudos(ModelForm):
    desc = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'placeholder': 'Descrição do conteúdo..'}))
    class Meta:
        model = Models.Conteudos
        fields = ['materia', 'desc','pdf']

class FormComentarios(ModelForm):
    autor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome do autor..'}))
    conteudo = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'placeholder': 'Seu comentário..'}))
    class Meta:
        model = Models.Comentarios
        fields = ['autor', 'conteudo']