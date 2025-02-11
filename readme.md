# Django Project Setup

## Requisitos
Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Virtualenvwrapper-win (para gerenciamento de ambientes virtuais)
- PostgreSQL (se necessário para o projeto)

## Instalação

1. **Clonar o repositório ou extrair os arquivos:**
   ```sh
   git clone <repositorio.git> myproject
   cd myproject
   ```
   *Ou extraia os arquivos do ZIP para um diretório adequado.*

2. **Criar um ambiente virtual usando Virtualenvwrapper-win:**
   ```sh
   mkvirtualenv myproject
   workon myproject
   ```

3. **Instalar dependências:**
   ```sh
   pip install django psycopg2 psycopg2-binary mongoengine
   ```

4. **Configurar o banco de dados:**
   - Para a Base de Dados em PostgreSQL, os scripts necessários estão na pasta SQL
   - Para a Base de Dados em MongoDB, os scripts necessários estão na pasta MongoDB-JSON
   - Após o uso dos scripts modifique os dados de conexão que se encontram na pasta `settings.py`, dentro do dirétorio `projbd2/projbd2/`:
     ```
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'postgres',
             'USER': 'postgres',
             'PASSWORD': '1234',
             'HOST': 'localhost',  # ou o endereço do servidor
             'PORT': '5432',       # porta padrão do PostgreSQL
         }
     }

     connect(
         db="BDII",
         host="localhost",
         port=27017,
     )
     ```
   - Aplicar migrações:
     ```sh
     python manage.py migrate
     ```

5. **Executar o servidor Django:**
   ```sh
   python manage.py runserver
   ```
   Acesse o projeto em `http://127.0.0.1:8000/`.

## Estrutura do Projeto
```
myproject/
│-- manage.py
│-- myapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
│   ├── migrations/
│-- templates/
│-- static/
```

## Contato
Caso tenha dúvidas, entre em contato com o responsável pelo projeto.

