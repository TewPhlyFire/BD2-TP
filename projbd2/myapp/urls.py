from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_login, name='home_page_login'),
    path('about_us/', views.about_us, name='about_us'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('remover-produto/<int:produto_id>/', views.remover_produto, name='remover_produto'),
    path('adicionar-produto/', views.adicionar_produto, name='adicionar_produto'),
    path('cesto/', views.cesto, name='cesto'),
    path('descobre-mais/<int:produto_id>/', views.descobre_mais, name='descobre_mais'),    
    path('detalhes-admin/<int:produto_id>/', views.detalhes_admin, name='detalhes_admin'),  # Corrigido
    path('folheto/', views.folheto, name='folheto'),
    path('login/', views.login, name='login'),
    path('registar/', views.registar, name='registar'),
    path('log_out/', views.log_out, name='log_out'),
    path('UserPage/<int:nif_cliente>/', views.UserPage, name='UserPage'),
    path('editar_perfil/<int:nif_cliente>/', views.editar_perfil, name='editar_perfil'),
    path('login_admin/', views.login_admin, name='login_admin'),

]

