# Jogoteca - Aplicativo Web com Flask

Este repositório contém o código-fonte do projeto **Jogoteca**, um aplicativo web desenvolvido em Python utilizando o microframework Flask. O projeto foi realizado através do curso **"Flask: crie uma webapp com Python"**, e tem como objetivo permitir a gestão de jogos, incluindo cadastro, listagem e login de usuários.

## Funcionalidades
- Listagem de jogos cadastrados.
- Cadastro de novos jogos.
- Autenticação de usuários.
- Sessão de usuários com Flask.
- Uso de mensagens flash para feedback ao usuário.

## Estrutura do Projeto
```
static/
    bootstrap.css

templates/
    lista.html
    login.html
    novo.html
    template.html

venv/

Jogo.py
jogoteca.py
Usuario.py
```

- **static/**: Contém arquivos estáticos, como folhas de estilo (CSS).
- **templates/**: Contém os templates HTML utilizados para renderizar as páginas do sistema.
- **venv/**: Ambiente virtual do Python (recomendado para isolar dependências).
- **Jogo.py**: Classe que representa um jogo.
- **Usuario.py**: Classe que representa um usuário.
- **jogoteca.py**: Arquivo principal da aplicação Flask.

## Instalação e Execução
1. Clone este repositório:
   ```sh
   git clone https://github.com/delberss/flask-webapp-jogoteca.git
   cd flask-webapp-jogoteca
   ```

2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências necessárias:
   ```sh
   pip install flask
   ```

4. Execute a aplicação:
   ```sh
   python jogoteca.py
   ```

5. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:5000
   ```

## Rotas da Aplicação
- `/` - Exibe a lista de jogos.
- `/novo` - Formulário para cadastrar um novo jogo (requer login).
- `/criar` - Rota que recebe os dados do formulário e adiciona um novo jogo.
- `/login` - Tela de login para autenticação de usuários.
- `/logout` - Realiza o logout do usuário.
- `/autenticar` - Valida as credenciais do usuário e inicia a sessão.

## Autenticação de Usuários
O sistema possui autenticação básica de usuários utilizando sessão do Flask. Usuários são armazenados em um dicionário e são identificados pelo nickname e senha.

## Tecnologias Utilizadas
- **Python 3**
- **Flask** (microframework web para Python)
- **HTML, CSS (Bootstrap)**

## Melhorias Futuras
- Integração com banco de dados.
- Melhor segurança na autenticação.
- Implementação de edição e remoção de jogos.
- Melhor layout com Bootstrap.

## Licença
Este projeto é de uso livre para fins educacionais.

