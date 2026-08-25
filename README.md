# Cartão de Identidade Acadêmica

# Sobre o projeto

O Cartão de Identidade Acadêmica é um sistema desenvolvido em Django que tem como objetivo criar uma representação digital dos alunos em formato de cartão de perfil.

Cada aluno possui informações como:

- Nome
- Curso
- Biografia

O projeto permite cadastrar alunos através do painel administrativo do Django e exibir seus cartões acadêmicos em uma interface web.

---

# Tecnologias utilizadas

- Python 3.13
- Django 6.1
- SQLite
- HTML5
- CSS3
- JavaScript

---

# Estrutura do projeto
CartaoAcademico
│
├── aluno
│ ├── migrations
│ ├── templates
│ │ └── aluno
│ │ └── lista.html
│ ├── admin.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── core
│ ├── settings.py
│ ├── urls.py
│ └── outros arquivos de configuração
│
├── db.sqlite3
├── manage.py
└── README.md
---

# Modelo de dados

O sistema possui o modelo **Aluno**, contendo:

| Campo | Tipo | Descrição |
|---|---|---|
| nome | CharField | Nome completo do aluno |
| curso | CharField | Curso do aluno |
| bio | TextField | Descrição, interesses ou objetivos do aluno |

---

# Como executar o projeto

# 1. Clonar o repositório
git clone URL_DO_REPOSITORIO


Entrar na pasta do projeto:
cd CartaoAcademico


---

# 2. Criar ambiente virtual
python -m venv venv


---

# 3. Ativar o ambiente virtual

Windows PowerShell:
venv\Scripts\Activate.ps1


---

# 4. Instalar as dependências
pip install django


---

# 5. Executar as migrações
python manage.py makemigrations
python manage.py migrate


---

# 6. Criar usuário administrador
python manage.py createsuperuser


Informe:

- Nome de usuário
- Email
- Senha

Esse usuário permitirá acessar o painel administrativo do Django.

---

# 7. Executar o servidor
python manage.py runserver

O projeto estará disponível em:
http://127.0.0.1:8000/


---

# Endpoints disponíveis

# Página dos cartões acadêmicos

Exibe todos os alunos cadastrados:
http://127.0.0.1:8000/alunos/


---

# Painel administrativo

Área para cadastrar, editar e remover alunos:
http://127.0.0.1:8000/admin/


---

# Funcionalidades

- Cadastro de alunos pelo Django Admin
- Armazenamento dos dados em banco SQLite
- Listagem dos alunos em cartões digitais
- Exibição de nome, curso e biografia
- Interface desenvolvida com HTML e CSS
- Tema escuro
- Alternância entre tema claro e escuro
- Animações e efeitos visuais nos cartões

---

# Interface

A página principal apresenta os alunos em formato de cartões acadêmicos, contendo:

- Nome do aluno
- Curso
- Biografia
- Design visual inspirado em uma ficha de identidade digital

---

# Banco de dados

O projeto utiliza SQLite como banco de dados padrão do Django.

O arquivo responsável pelo banco é:
db.sqlite3


---

# Desenvolvimento

Projeto desenvolvido para a disciplina de **Programação Backend utilizando Python e Django**.

Objetivo: construir um sistema backend para gerenciamento e apresentação de perfis acadêmicos digitais.

---

# Autor

Nome: Vitor Faria de Oliveira e Silva 

Curso: Sistemas de Informação




# Demonstração

# Página dos cartões acadêmicos

![Página dos cartões 1](screenshots/alunos_1.png)

![Página dos cartões 2](screenshots/alunos_2.png)

Acesse:
http://127.0.0.1:8000/alunos/


# Painel administrativo

![Admin 1](screenshots/admin_1.png)

![Admin 2](screenshots/admin_2.png)

![Admin 3](screenshots/admin_3.png)

Acesse:
http://127.0.0.1:8000/admin/