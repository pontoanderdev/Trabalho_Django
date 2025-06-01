
from django.urls import path
from . import views

urlpatterns = [
    
    path('usuarios/', views.cliente_list, name='cliente_list'),
    path('usuarios/novo/', views.cliente_create, name='cliente_create'),
    path('usuario/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('usuario/<int:pk>/excluir/', views.cliente_delete, name='cliente_delete'),

    
    path('sale/', views.venda_list, name='venda_list'),
    path('sale/nova/', views.venda_create, name='venda_create'),
    path('sale/<int:pk>/editar/', views.venda_update, name='venda_update'),
    path('sale/<int:pk>/excluir/', views.venda_delete, name='venda_delete'),
]
