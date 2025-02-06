
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

# View para a página 'UserPage'
def UserPage(request, nif_cliente):
    with connection.cursor() as cursor:
        cursor.execute("SELECT pnome_cliente, unome_cliente, morada, mail, contacto_tel FROM cliente WHERE nif_cliente = %s", [nif_cliente])
        row = cursor.fetchone()

    if row:
        cliente = {
            'nif_cliente': nif_cliente,
            'pnome_cliente': row[0],
            'unome_cliente': row[1],
            'morada': row[2],
            'mail': row[3],
            'contacto_tel': row[4],
        }
    else:
        cliente = None  # Se não encontrar o cliente, evita erro

    return render(request, 'UserPage.html', {'cliente': cliente})


# Editar perfil
def editar_perfil(request, nif_cliente):
    if request.method == "POST":
        pnome_cliente = request.POST.get("pnome_cliente")
        unome_cliente = request.POST.get("unome_cliente")
        morada = request.POST.get("morada")
        mail = request.POST.get("mail")
        contacto_tel = request.POST.get("contacto_tel")

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE cliente 
                SET pnome_cliente = %s, unome_cliente = %s, morada = %s, mail = %s, contacto_tel = %s 
                WHERE nif_cliente = %s
            """, [pnome_cliente, unome_cliente, morada, mail, contacto_tel, nif_cliente])

        return redirect('UserPage', nif_cliente=nif_cliente)

    return redirect('UserPage', nif_cliente=nif_cliente)

# View para a página 'Login'
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        with connection.cursor() as cursor:
            cursor.execute("select * from cliente where mail = %s and password_client = %s", [username, password])
            cliente = cursor.fetchone()
            if cliente is not None:
                request.session['cliente'] = cliente
                return redirect('home_page_login')
    if 'cliente' in request.session:
        return redirect('home_page_login')

    return render(request, 'login.html')

def log_out(request):
    if 'cliente' in request.session:
        del request.session['cliente']
    return redirect('login')

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
