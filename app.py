import os

from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gerar_ideia', methods=['POST'])
def gerar_ideia():
    input_usuario = request.form.get('input')
    # Chamada à API do ChatGPT
    try:
        # Definindo o contexto do tema
        tema = '''Gerar ideias inovadoras para startups com o auxilio da expertise dos profissionais da ResumoCast.
        oferecendo cursos, programas de buildagem e outras iniciativas educativas, 
        todas projetadas para impulsionar o desenvolvimento pessoal e profissional. 
        Com anos de experiência e um histórico comprovado no ecossistema empreendedor, 
        a ResumoCast Ventures se estabeleceu como uma referência no mercado, 
        ajudando a moldar a próxima geração de líderes empresariais no Brasil.
        Para gerar ideias inovadoras para startups, 
        é essencial observar problemas cotidianos e identificar lacunas que ainda não foram resolvidas ou que podem ser abordadas de maneira mais eficiente. 
        A pesquisa de tendências emergentes, como novas tecnologias ou mudanças no comportamento dos consumidores, pode inspirar soluções criativas. 
        Conversar com potenciais usuários e entender suas dores também é uma excelente maneira de descobrir oportunidades inexploradas. Além disso, 
        colaborar com profissionais de diferentes áreas pode gerar insights únicos ao combinar conhecimentos diversos. Por fim, 
        estar disposto a experimentar e ajustar ideias com base em feedback real é fundamental para transformar conceitos inovadores em startups de sucesso.
        '''

        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": tema}, # Definindo o tema na mensagem do sistema
                {"role": "user", "content": f"Crie uma ideia de startup baseada no seguinte input: {input_usuario}"}
            ],
            max_tokens=150
        )

        ideia = response['choices'][0]['message']['content']
        return jsonify({"ideia": ideia})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
