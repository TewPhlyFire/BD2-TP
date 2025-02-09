
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Cliente, Promo, ProdutoImagem
from django.db import connection
from .forms import RegistroForm
import json
import base64

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
        nome = request.POST["nome"]
        quantidade = request.POST["quantidade"]
        categoria = request.POST["categoria"]
        preco = request.POST["preco"]
        desc = request.POST["descricao"]
        imagem = request.FILES.get("imagem")  # Obtém a imagem do formulário

        # Inserir o produto no PostgreSQL
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO produto (nome_produto, descricao, preco, id_subcategoria, quantidade) 
                VALUES (%s, %s, %s, %s, %s) RETURNING id_produto
                """,
                [nome, desc, preco, categoria, quantidade],
            )
            id_produto = cursor.fetchone()[0]  # Obtém o ID do produto recém-criado

        # Se houver uma imagem, salvar no MongoDB
        if imagem:
            imagem_binaria = imagem.read()  # Lê a imagem em formato binário
            produto_imagem = ProdutoImagem(
                id_prodref=id_produto,  # Salva o ID do PostgreSQL no MongoDB
                imagens=imagem_binaria
            )
            produto_imagem.save()

        return redirect("admin_page")  # Redireciona para a página principal

    categorias = Categoria.objects.all()
    return render(request, "AdicionarProduto.html", {"categorias": categorias})


# View para a página 'Cesto'
def cesto(request):
    # Supondo que você tenha um modelo Produto no Django
    produtos = Produto.objects.all()  # Obtenha todos os produtos disponíveis
    produtos_json = json.dumps([produto.to_dict() for produto in produtos])
    return render(request, 'cesto.html', {'produtos': produtos_json})

# View para a página 'DescobreMais'
def descobre_mais(request, produto_id):
    # Recupera o produto com o id fornecido
    produto = Produto.objects.get(id_produto=produto_id)
    return render(request, 'DescobreMais.html', {'produto': produto})
# View para a página 'DetalhesAdmin'
def detalhes_admin(request, produto_id):
    # Recupera o produto com base no ID do PostgreSQL
    produto = get_object_or_404(Produto, id_produto=produto_id)  

    if request.method == "POST":
        nome = request.POST['nome']
        quantidade = request.POST['quantidade']
        categoria = request.POST['categoria']
        preco = request.POST['preco']
        desc = request.POST['descricao']
        imagem = request.FILES.get("imagem")  # Obtém a imagem se foi enviada

        # Atualiza o produto no banco de dados
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE produto SET nome_produto = %s, descricao = %s, preco = %s, id_subcategoria = %s, quantidade = %s WHERE id_produto = %s",
                [nome, desc, preco, categoria, quantidade, produto_id]
            )

        # Se uma nova imagem foi enviada, atualizamos no MongoDB
        if imagem:
            imagem_binaria = imagem.read()
            
            # Verificar se a imagem já existe no MongoDB
            produto_imagem = ProdutoImagem.objects(id_prodref=produto_id).first()
            if produto_imagem:
                produto_imagem.imagens = imagem_binaria  # Atualiza a imagem existente
                produto_imagem.save()
            else:
                # Cria um novo registro no MongoDB
                nova_imagem = ProdutoImagem(
                    id_prodref=produto_id,
                    imagens=imagem_binaria
                )
                nova_imagem.save()

    # Buscar a imagem no MongoDB
    produto_imagem = ProdutoImagem.objects(id_prodref=produto.id_produto).first()
    imagem_base64 = base64.b64encode(produto_imagem.imagens).decode("utf-8") if produto_imagem else None

    categorias = Categoria.objects.all()

    return render(
        request, 
        "DetalhesAdmin.html", 
        {"produto": produto, "categorias": categorias, "imagem": imagem_base64}
    )

# View para a página 'Folheto'
def folheto(request):
    promos = Produto.objects.all()
    return render(request, 'Folheto.html', {'promos': promos})

    # View para a página 'HomePageLogin'
def home_page_login(request):
    promos = Promo.objects.all()
    produtos = Produto.objects.all()
    categories = Categoria.objects.all()
    return render(request, 'HomePageLogin.html', {'produtos': produtos, 'categories': categories, 'promos': promos})

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

        try:
            cliente = Cliente.objects.get(mail=username, password_client=password)

            # Criar um dicionário com os dados do cliente
            user_data = {
                'nif': cliente.nif_cliente,
                'nome': cliente.pnome_cliente,
                'sobrenome': cliente.unome_cliente,
                'telefone': cliente.contacto_tel,
                'morada': cliente.morada,
                'email': cliente.mail,
            }
            print(user_data)
            # Salvar os dados na sessão do Django
            
            request.session['cliente'] = user_data  
            print(request.session.get('cliente'))
            

        except Cliente.DoesNotExist:
            return render(request, 'login.html', {'error_message': "Utilizador ou senha incorretos."})

    return render(request, 'login.html')

def log_out(request):
    if 'cliente' in request.session:
        del request.session['cliente']
    return redirect('login')

#login funcionarios
def login_admin(request):
    if request.method == 'POST':
        pnome_funcionario = request.POST.get('pnome_funcionario')
        senha_funcionario = request.POST.get('senha_funcionario')

        with connection.cursor() as cursor:
            cursor.execute("select * from funcionario where pnome_funcionario = %s and senha_funcionario = %s", [pnome_funcionario, senha_funcionario])
            funcionario = cursor.fetchone()
            if funcionario is not None:
                request.session['funcionario'] = funcionario
                return redirect('admin_page')

    return render(request, 'login_admin.html')


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


# View para a página 'Registrar'
def registrar(request):
    return render(request, 'Registrar.html')
