
from django.shortcuts import render, redirect
from .models import Produto, Categoria, Cliente
from django.db import connection
from .forms import RegistroForm

# View para a página 'AboutUs'
def about_us(request):
    return render(request, 'AboutUs.html')

# View para a página 'AdminPage'
def admin_page(request):
    # Recupera todos os produtos
    produtos = Produto.objects.all()

    return render(request, 'AdminPage.html', {'produtos': produtos})


def remover_produto(request, produto_id):
    with connection.cursor() as cursor:
        cursor.execute("delete from produto where id_produto = %s", [produto_id])
    return redirect('admin_page') 
 # Redireciona de volta para a página de administração
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
def descobre_mais(request, produto_id):
    # Recupera o produto com o id fornecido
    produto = Produto.objects.get(id_produto=produto_id)
    return render(request, 'DescobreMais.html', {'produto': produto})
# View para a página 'DetalhesAdmin'
def detalhes_admin(request, produto_id):
    # Recupera o produto com base no ID
    produto = Produto.objects.get(id_produto=produto_id)  

    if request.method == "POST":
        nome = request.POST['nome']
        quantidade = request.POST['quantidade']
        categoria = request.POST['categoria']
        preco = request.POST['preco']
        desc = request.POST['descricao']
        
        # Atualiza o produto no banco de dados
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE produto SET nome_produto = %s, descricao = %s, preco_produto = %s, id_subcategoria = %s, quantidade = %s WHERE id_produto = %s",
                [nome, desc, preco, categoria, quantidade, produto_id]
            )
    categoria = Categoria.objects.all()
    
    return render(request, 'DetalhesAdmin.html', {'produto': produto, 'categorias': categoria})


# View para a página 'Folheto'
def folheto(request):
    promos = Produto.objects.all()
    return render(request, 'Folheto.html', {'promos': promos})
    # View para a página 'HomePageLogin'
def home_page_login(request):
    promos = Produto.objects.all()
    categories = Categoria.objects.all()
    return render(request, 'HomePageLogin.html', {'promos': promos, 'categories': categories})

# View para a página 'Login'
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('HomePageLogin')  # Redirecionamento após login bem-sucedido
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'login.html')

def registar(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        print("Formulário inválido")
        form = RegistroForm()

    return render(request, 'register.html', {'form': form})

# View para a página 'PagarCenas'
def pagar_cenas(request):
    return render(request, 'PagarCenas.html')

# View para a página 'Registrar'
def registrar(request):
    return render(request, 'Registrar.html')
