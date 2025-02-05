
from django.shortcuts import render
from .models import Produto, Categoria
from django.db import connection

# View para a página 'AboutUs'
def about_us(request):
    return render(request, 'AboutUs.html')

# View para a página 'AdminPage'
def admin_page(request):
    return render(request, 'AdminPage.html')

# View para a página 'AdicionarProduto'
def adicionar_produto(request):
    if request.method == "POST":
        nome = request.POST['nome']
        quantidade = request.POST['quantidade']
        categoria = request.POST['categoria']
        preco = request.POST['preco']
        desc = request.POST['descricao']
        with connection.cursor() as cursor:
            cursor.execute("insert into produto (nome_produto, descricao, preco_produto, id_subcategoria, quantidade) values (%s, %s, %s, %s, %s)", [nome, desc, preco, categoria, quantidade])
        
    categorias = Categoria.objects.all()
    return render(request, 'AdicionarProduto.html', {'categorias': categorias})

# View para a página 'ApoioCliente'
def apoio_cliente(request):
    return render(request, 'ApoioCliente.html')

# View para a página 'Cesto'
def cesto(request):
    return render(request, 'Cesto.html')

# View para a página 'CestoNoLogin'
def cesto_no_login(request):
    return render(request, 'CestoNoLogin.html')

# View para a página 'DescobreMais'
def descobre_mais(request):
    return render(request, 'DescobreMais.html')

# View para a página 'DetalhesAdmin'
def detalhes_admin(request):
    return render(request, 'DetalhesAdmin.html')

# View para a página 'Folheto'
def folheto(request):
    return render(request, 'Folheto.html')
    # View para a página 'HomePageLogin'
def home_page_login(request):
    promos = Produto.objects.all()
    categories = Categoria.objects.all()
    return render(request, 'HomePageLogin.html', {'promos': promos, 'categories': categories})

# View para a página 'Login'
def login(request):
    return render(request, 'Login.html')

# View para a página 'PagarCenas'
def pagar_cenas(request):
    return render(request, 'PagarCenas.html')

# View para a página 'Registrar'
def registrar(request):
    return render(request, 'Registrar.html')
