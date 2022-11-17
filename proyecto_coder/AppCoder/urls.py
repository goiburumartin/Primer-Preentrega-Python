from django.urls import path

from AppCoder import views


urlpatterns = [
    #path('', views.index, name="Index"),
    path('', views.inicio, name="Inicio"), 
    path('seguidores', views.seguidores, name="Seguidores"),
    path('eventos', views.eventos, name="Eventos"),
    path('paginas', views.paginas, name="Paginas"),
    path('PaginaFormulario', views.PaginaFormulario, name="PaginaFormulario"),
    path('EventoFormulario',  views.EventoFormulario, name="EventoFormulario"),
    path('SeguidorFormulario',  views.SeguidorFormulario, name="SeguidorFormulario"),
    path('buscar_pagina/', views.buscar_pagina),

]