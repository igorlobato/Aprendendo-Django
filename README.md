# Gerenciamento de Tarefas com Django

## Descrição
Este é um aplicativo de gerenciamento de tarefas desenvolvido com Django, que inclui funcionalidades de autenticação de usuários, gerenciamento de tarefas, categorias e etiquetas, notificações por e-mail e uma API REST. O objetivo deste projeto é demonstrar habilidades no desenvolvimento web utilizando Django.

## Funcionalidades

1. **Autenticação de Usuários**:
   - Registro de usuários
   - Login e logout
   - Recuperação de senha

2. **Gestão de Tarefas**:
   - Criar, editar e excluir tarefas
   - Marcar tarefas como concluídas
   - Atribuir tarefas a diferentes usuários

3. **Categorias e Etiquetas**:
   - Criar categorias e etiquetas para organizar tarefas

4. **Dashboard e Visualização de Tarefas**:
   - Exibir tarefas pendentes, concluídas e futuras em um dashboard
   - Filtrar tarefas por data, categoria ou etiqueta

5. **Notificações e Lembretes**:
   - Notificações por e-mail para lembretes de tarefas próximas do prazo

6. **API REST**:
   - Endpoints para permitir integração com outras aplicações

7. **Interface de Usuário (UI)**:
   - Interface amigável utilizando Django Templates ou uma integração com um frontend como React/Vue.js (opcional)

## Tecnologias Utilizadas

- **Django**: Backend e sistema de templates
- **Django REST Framework**: API REST
- **Celery**: Tarefas assíncronas e agendamento de lembretes
- **Bootstrap**: Interface de usuário (ou outro framework CSS)
- **SQLite**: Banco de dados (para desenvolvimento, considere PostgreSQL para produção)
- **Git**: Controle de versão
- **GitHub**: Hospedagem do código

## Instalação

### Pré-requisitos
- Python 3.x
- pip
- Virtualenv (opcional, mas recomendado)

### Passos para Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/igorlobato/Aprendendo-Django
    cd Aprendendo-Django
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações:
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Utilização

- Acesse o aplicativo em `http://127.0.0.1:8000`
- Faça login com sua conta
- Gerencie suas tarefas, categorias e etiquetas
- Configure notificações e lembretes

## API REST

A API REST permite integração com outras aplicações. A documentação dos endpoints pode ser encontrada em `http://127.0.0.1:8000/api-docs`.