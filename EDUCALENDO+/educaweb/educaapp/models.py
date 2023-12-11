from django.db import models

class Materias(models.Model):
    def __str__(self):
        return str(self.nome)

    nome = models.CharField(max_length=60)
    prof = models.CharField(max_length=60)
    sala_num = models.IntegerField()

class Conteudos(models.Model):
    materia =  models.ForeignKey(Materias, related_name='nome_materia', on_delete=models.CASCADE)
    desc = models.CharField(max_length=5000)
    pdf = models.FileField('pdf', upload_to='doc_conteudos')

class Comentarios(models.Model):
    id_conteudo = models.IntegerField(default=0)
    autor = models.CharField(max_length=60)
    conteudo = models.CharField(max_length=5000)