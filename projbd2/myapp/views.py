
from django.shortcuts import render
from .models import Produto, Categoria

# View para a página 'AboutUs'
def about_us(request):
    return render(request, 'myapp/AboutUs.html')

# View para a página 'AdminPage'
def admin_page(request):
    return render(request, 'myapp/AdminPage.html')

# View para a página 'AdicionarProduto'
def adicionar_produto(request):
    return render(request, 'myapp/AdicionarProduto.html')

# View para a página 'ApoioCliente'
def apoio_cliente(request):
    return render(request, 'myapp/ApoioCliente.html')

# View para a página 'Cesto'
def cesto(request):
    return render(request, 'myapp/Cesto.html')

# View para a página 'CestoNoLogin'
def cesto_no_login(request):
    return render(request, 'myapp/CestoNoLogin.html')

# View para a página 'DescobreMais'
def descobre_mais(request):
    return render(request, 'myapp/DescobreMais.html')

# View para a página 'DetalhesAdmin'
def detalhes_admin(request):
    return render(request, 'myapp/DetalhesAdmin.html')

# View para a página 'Folheto'
def folheto(request):
    return render(request, 'myapp/Folheto.html')
    # View para a página 'HomePageLogin'
def home_page_login(request):
    promos = Produto.objects.all()
    categories = Categoria.objects.all()
    return render(request, 'myapp/HomePageLogin.html', {'promos': promos, 'categories': categories})

# View para a página 'Login'
def login(request):
    return render(request, 'myapp/Login.html')

# View para a página 'PagarCenas'
def pagar_cenas(request):
    return render(request, 'myapp/PagarCenas.html')

# View para a página 'Registrar'
def registrar(request):
    return render(request, 'myapp/Registrar.html')
