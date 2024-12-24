from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_login, name='home_page_login'),
    path('about_us/', views.about_us, name='about_us'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('adicionar-produto/', views.adicionar_produto, name='adicionar_produto'),
    path('apoio-cliente/', views.apoio_cliente, name='apoio_cliente'),
    path('cesto/', views.cesto, name='cesto'),
    path('cesto-no-login/', views.cesto_no_login, name='cesto_no_login'),
    path('descobre-mais/', views.descobre_mais, name='descobre_mais'),
    path('detalhes-admin/', views.detalhes_admin, name='detalhes_admin'),
    path('folheto/', views.folheto, name='folheto'),
    path('login/', views.login, name='login'),
    path('pagar-cenas/', views.pagar_cenas, name='pagar_cenas'),
    path('registrar/', views.registrar, name='registrar'),
]
