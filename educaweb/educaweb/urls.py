from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from educaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ver_materias, name='ver_materias'),
    path('conteudos/', views.ver_conteudos, name='ver_conteudos'),
    path('avisos/', views.ver_avisos, name='ver_avisos'),
    path('detalhes/<int:pk>/', views.ver_detalhes, name='ver_detalhes'),
    path('addmateria/', views.create_materia, name='create_materia'),
    path('addcomentario/', views.create_comentario, name='create_comentario'),
    path('addconteudo/', views.create_conteudo, name='create_conteudo'),
    path('editdesc/<int:pk>/', views.edit_descricao, name='edit_descricao'),
    path('updatedesc/<int:pk>/', views.update_descricao, name='update_descricao'),
    path('deleteconteudo/<int:pk>/', views.delete_conteudo, name='delete_conteudo'),
    path('deletemateria/<int:pk>/', views.delete_materia, name='delete_materia'),
    path('deletecomentario/<int:pk>/', views.delete_comentario, name='delete_comentario'),
]

if settings.DEBUG:
    urlpatterns += static (
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT)