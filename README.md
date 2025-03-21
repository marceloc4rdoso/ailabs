# Gerador de Ideias para Startups

Este projeto usa a API do ChatGPT para gerar conceitos inovadores de startups com base em descrições fornecidas pelos usuários.
### Video de apresentação do projeto

<a href="https://www.youtube.com/watch?v=3GFzRlXWTaw" target="_blank">
  <img src="https://img.youtube.com/vi/3GFzRlXWTaw/default.jpg" alt="   Assista o vídeo no Youtube" width="200" height="100" />
</a>

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/marceloc4rdoso/ailabs.git

2. Criação do Ambiente Virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
3. Estrutura do Projeto:
   ```bash
   projeto_startup/
   ├── .env (deve ser inserido com sua api key)
   ├── app.py
   ├── README.md
   ├── requirements.txt
   ├── static/
   │   └── img
   │   └── scripts.js
   │   └── style.csss
   ├── templates/
       └── index.html   
   
4. Arquivo .env: No arquivo .env, armazene sua chave de API:
   ```bash
   OPENAI_API_KEY='sua_openai_api_key_aqui'
5. Inicie a aplicação:
   ```bash
   python app.py
6. Acesse a aplicação em http://localhost:5001  

### OBS.: **Requisitos e Considerações**
- **Chave da API**: Certifique-se de manter a chave da OpenAI em local seguro (como um arquivo `.env`).
- **Limites de uso**: A API da OpenAI tem limites de uso, por isso é importante monitorar o uso de tokens.
#### Créditos do CSS criado pela [https://github.com/anapamponet]
 

### **Manual de uso**
Acesse a página principal e insira um conceito ou área para a qual deseja gerar uma ideia de startup.
Clique em "Gerar Ideia" e aguarde a sugestão.

### Desenvolvedores 
#### Licença
Este projeto está licenciado sob a MIT License.
#### Como Usar
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
####Caso necessite
   ```bash   
      ### Passo 5: Adicionar `requirements.txt`
      Gere o `requirements.txt` para que outros possam instalar as dependências com facilidade:
      ```bash
      pip freeze > requirements.txt



