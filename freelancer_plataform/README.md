# Freelancer Platform

Este projeto é uma plataforma para freelancers, permitindo que usuários se cadastrem, visualizem freelancers disponíveis e façam login para acessar funcionalidades adicionais.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

- **app.py**: Ponto de entrada da aplicação. Configura o servidor web, define as rotas e gerencia a lógica do aplicativo.
- **requirements.txt**: Lista as dependências do projeto que precisam ser instaladas para que a aplicação funcione corretamente.
- **templates/base.html**: Estrutura base do HTML da aplicação, incluindo a configuração do cabeçalho, links para CSS e a barra de navegação.
- **templates/index.html**: Página inicial da aplicação, que estende o `base.html` e define o conteúdo específico da página inicial.
- **static/css/style.css**: Estilos CSS personalizados para a aplicação, permitindo a personalização da aparência.
- **static/img/favicon.ico**: Ícone da aplicação que aparece na aba do navegador.
- **static/img/logo.png**: Imagem do logotipo da aplicação, utilizada na barra de navegação.

## Como Executar

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   ```

2. Navegue até o diretório do projeto:
   ```
   cd freelancer_plataform
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```
   python app.py
   ```

A aplicação estará disponível em `http://127.0.0.1:5000/`.