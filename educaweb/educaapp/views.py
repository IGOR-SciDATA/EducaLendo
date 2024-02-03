from django.shortcuts import render,redirect
from educaapp import forms
from educaapp.models import *
from django.contrib.auth import login as log
from django.contrib.auth import authenticate,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def ver_materias(request):
    data = {}
    data['form'] = forms.FormMaterias()
    data['materias'] = Materias.objects.all()
    return render(request, 'materias.html', data)

def ver_usuarios(request):
    data = {}
    data['usuarios'] = User.objects.all()
    return render(request, 'usuarios.html', data)

def ver_login(request):
    data = {}
    data['materias'] = Materias.objects.all()
    return render(request, 'login.html', data)

def verif_login(request):
    user = authenticate(username=request.POST['user'], password=request.POST['pass'])
    if user is not None:
       log(request, user)
       return redirect('/vermaterias/')
    else:
       data = {}
       data['msg'] = 'Usuário ou Senha incorreto!'
       data['class'] = 'alert-danger'
       return render(request, 'login.html', data)

def ver_conteudos(request):
    data = {}
    data['form'] = forms.FormConteudos()
    data['conteudos'] = Conteudos.objects.all().order_by('-id')
    return render(request, 'conteudos.html', data)

def ver_detalhes(request, pk):
    data = {}
    data['form'] = forms.FormComentarios()
    data['conteudos'] = Conteudos.objects.get(id=pk)
    data['comentarios'] = Comentarios.objects.filter(id_conteudo=pk).order_by('-id')
    return render(request, 'detalhes.html', data)


def edit_descricao(request, pk):
    data = {}
    data['db'] = Conteudos.objects.get(id=pk)
    data['form'] = forms.FormConteudos(instance=data['db'])
    return render(request, 'detalhes.html', data)

def ver_avisos(request):
    return render(request, 'materias.html')

def create_materia(request):
   form = forms.FormMaterias(request.POST)
   if form.is_valid():
      form = form.save(commit=False)
      form.save()
      return redirect('ver_materias')

def create_conteudo(request):
   form = forms.FormConteudos(request.POST, request.FILES)
   if form.is_valid():
      form = form.save(commit=False)
      form.save()
      return redirect('ver_conteudos')

def create_comentario(request):
   form = forms.FormComentarios(request.POST)
   id = request.POST.get('conteudoid')
   if form.is_valid():
      form = form.save(commit=False)
      form.id_conteudo = id
      form.save()
      referer1 = request.META.get('HTTP_REFERER', None)
      return redirect(referer1)
   
def update_descricao(request, pk):
   data = {}
   data['db'] = Conteudos.objects.get(id=pk)
   form = forms.FormConteudos(request.POST, request.FILES, instance=data['db'])

   if form.is_valid():
      form = form.save(commit=False)
      form.save()
      return redirect('ver_conteudos')

def delete_conteudo(request, pk):
   bd = Conteudos.objects.get(id=pk)
   bd.delete()
   return redirect('ver_conteudos')

def delete_materia(request, pk):
   bd = Materias.objects.get(id=pk)
   bd.delete()
   return redirect('ver_materias')

def delete_comentario(request, pk):
   bd = Comentarios.objects.get(id=pk)
   bd.delete() 
   referer1 = request.META.get('HTTP_REFERER', None)
   return redirect(referer1)