
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Cliente, Promo, ProdutoImagem
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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
    produtos = Produto.objects.all()
    produtos_lista = []

    for produto in produtos:
        produto_imagem = ProdutoImagem.objects(id_prodref=produto.id_produto).first()
        imagem_base64 = base64.b64encode(produto_imagem.imagens).decode("utf-8") if produto_imagem else None

        produtos_lista.append({
            "id_produto": produto.id_produto,
            "nome_produto": produto.nome_produto,
            "preco_produto": float(produto.preco),
            "imagem": imagem_base64,
            "stock": produto.quantidade  # Inclui o estoque no JSON
        })

    produtos_json = json.dumps(produtos_lista)
    return render(request, 'cesto.html', {'produtos': produtos_json})


@csrf_exempt
def finalizar_compra(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Aqui você pode processar os dados da compra
            itens = data.get('itens', [])
            morada = data.get('morada', '')
            nif = data.get('nif', '')

            # Lógica de processamento da compra
            # Exemplo de atualização do estoque e salvar a compra, etc.

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)

# View para a página 'DescobreMais'
def descobre_mais(request, produto_id):
    # Recupera o produto do PostgreSQL
    produto = get_object_or_404(Produto, id_produto=produto_id)

    # Buscar a imagem no MongoDB associada ao produto
    produto_imagem = ProdutoImagem.objects(id_prodref=produto.id_produto).first()
    
    # Converter a imagem para Base64 para exibição no template
    imagem_base64 = base64.b64encode(produto_imagem.imagens).decode("utf-8") if produto_imagem else None

    return render(request, 'DescobreMais.html', {
        'produto': produto,
        'imagem': imagem_base64  # Passamos a imagem para o template
    })

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
    promos = Promo.objects.all()
    produtos = Produto.objects.all()

    # Criar um dicionário de imagens associadas aos produtos
    imagens_produtos = {}
    for produto in produtos:
        produto_imagem = ProdutoImagem.objects(id_prodref=produto.id_produto).first()
        if produto_imagem:
            imagens_produtos[produto.id_produto] = base64.b64encode(produto_imagem.imagens).decode("utf-8")

    return render(
        request, 
        'Folheto.html', 
        {
            'produtos': produtos, 
            'promos': promos,
            'imagens_produtos': imagens_produtos  # Passamos o dicionário para o template
        }
    )
    

    # View para a página 'HomePageLogin'
def home_page_login(request):
    promos = Promo.objects.all()
    produtos = Produto.objects.all()
    categories = Categoria.objects.all()

    # Criar um dicionário de imagens associadas aos produtos
    imagens_produtos = {}
    for produto in produtos:
        produto_imagem = ProdutoImagem.objects(id_prodref=produto.id_produto).first()
        if produto_imagem:
            imagens_produtos[produto.id_produto] = base64.b64encode(produto_imagem.imagens).decode("utf-8")

    return render(
        request, 
        'HomePageLogin.html', 
        {
            'produtos': produtos, 
            'categories': categories, 
            'promos': promos,
            'imagens_produtos': imagens_produtos  # Passamos o dicionário para o template
        }
    )
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






def listar_promocoes(request):
    # Buscar promoções existentes
    promocoes = Promo.objects.all()
    produtos = Produto.objects.all()  # Produtos para criação de promoções

    if request.method == "POST":
        id_produto = request.POST["id_produto"]
        data_inicio = request.POST["data_inicio"]
        data_fim = request.POST["data_fim"]
        desconto = request.POST["desconto"]

        # Inserir a nova promoção no banco de dados
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO promo (id_produto, data_inicio, data_fim, desconto) 
                VALUES (%s, %s, %s, %s)
                """,
                [id_produto, data_inicio, data_fim, desconto],
            )

        return redirect("listar_promocoes")

    return render(request, "Promolist.html", {"promocoes": promocoes, "produtos": produtos})


def editar_promocao(request, promo_id):
    promocao = get_object_or_404(Promo, id_promo=promo_id)
    produtos = Produto.objects.all()

    if request.method == "POST":
        id_produto = request.POST["id_produto"]
        data_inicio = request.POST["data_inicio"]
        data_fim = request.POST["data_fim"]
        desconto = request.POST["desconto"]

        # Atualizar a promoção no banco de dados
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE promo 
                SET id_produto = %s, data_inicio = %s, data_fim = %s, desconto = %s
                WHERE id_promo = %s
                """,
                [id_produto, data_inicio, data_fim, desconto, promo_id],
            )

        return redirect("listar_promocoes")

    return render(request, "editar_promocao.html", {"promocao": promocao, "produtos": produtos})


def excluir_promocao(request, promo_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM promo WHERE id_promo = %s", [promo_id])

    return redirect("listar_promocoes")

