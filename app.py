# Importamos a biblioteca SQLite3, que permite a criação e o uso de um banco de dados local
import sqlite3  

# Importamos os recursos do Flask:
# - Flask: para criar a aplicação web
# - request: para acessar os dados que o usuário envia para a API
# - jsonify: para devolver os dados em formato JSON (estrutura de texto compreensível por máquinas)
from flask import Flask, request, jsonify  
from flask_cors import CORS

# Criamos a aplicação Flask.
# O parâmetro "__name__" informa que este é o arquivo principal da aplicação.
app = Flask(__name__)
CORS(app)
# 🔹 Criamos uma rota que responde ao endereço "/femandaopix"
# Quando alguém acessar http://127.0.0.1:5000/femandaopix no navegador, a função abaixo será executada
@app.route("/femandaopix")
def manda_o_pix():
    # Ao acessar a rota, o navegador vai exibir essa frase formatada com HTML (<h2>)
    return "<h2>SE TEM DOR DE CUTUVELO, TÁ DEVENDO</h2>"

# 🔹 Criamos uma função que será responsável por iniciar o banco de dados
# Ela garante que o arquivo database.db seja criado e que a tabela LIVROS esteja pronta para uso
def init_db():
    # Abrimos a conexão com o banco de dados (ou criamos o arquivo se ele não existir)
    # O "with" é usado para garantir que a conexão seja fechada automaticamente após o uso
    with sqlite3.connect("database.db") as conn:
        # Executamos um comando SQL para criar a tabela LIVROS, caso ela ainda não exista
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único para cada livro, gerado automaticamente
                    titulo TEXT NOT NULL,                 -- Título do livro (não pode ser vazio)
                    categoria TEXT NOT NULL,              -- Categoria (ex: Aventura, Programação)
                    autor TEXT NOT NULL,                  -- Nome do autor
                    image_url TEXT NOT NULL               -- URL da imagem do livro
                )
            """
        )

# Chamamos a função init_db para garantir que a tabela exista antes de usarmos a API
init_db()

# 🔹 Criamos uma rota POST para cadastrar um novo livro na base de dados
@app.route("/doar", methods=["POST"])
def doar():
    # Pegamos os dados que o cliente enviou no corpo da requisição, no formato JSON
    dados = request.get_json()

    # Verificamos se dados é uma lista ou um único objeto
    if isinstance(dados, list):
        # Se for uma lista, processamos cada livro individualmente
        resultados = []
        for livro in dados:
            # Extraímos cada campo enviado
            titulo = livro.get("titulo")
            categoria = livro.get("categoria")
            autor = livro.get("autor")
            image_url = livro.get("image_url")

            # Verificamos se todos os campos foram preenchidos corretamente
            if not titulo or not categoria or not autor or not image_url:
                return jsonify({"Erro":"Todos os campos são obrigatórios"}), 400

            # Abrimos uma conexão com o banco de dados
            with sqlite3.connect("database.db") as conn:
                # Executamos um comando SQL para inserir os dados recebidos na tabela LIVROS
                conn.execute(f"""
                    INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
                    VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
                """)
                
                # Salvamos as alterações no banco
                conn.commit()
                
                resultados.append({"titulo": titulo, "status": "cadastrado com sucesso"})
        
        # Retornamos uma mensagem de sucesso com o status 201 (Created)
        return jsonify({"mensagem": "Livros cadastrados com sucesso", "resultados": resultados}), 201
    else:
        # Se for um único objeto, processamos normalmente
        titulo = dados.get("titulo")
        categoria = dados.get("categoria")
        autor = dados.get("autor")
        image_url = dados.get("image_url")

        # Verificamos se todos os campos foram preenchidos corretamente
        if not titulo or not categoria or not autor or not image_url:
            # Caso algum campo esteja faltando, retornamos um erro 400 com uma mensagem
            return jsonify({"Erro":"Todos os campos são obrigatórios"}), 400 

        # Abrimos uma conexão com o banco de dados
        with sqlite3.connect("database.db") as conn:
            # Executamos um comando SQL para inserir os dados recebidos na tabela LIVROS
            conn.execute(f"""
                INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
                VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
            """)

            # Salvamos as alterações no banco com o commit()
            conn.commit()

            # Retornamos uma mensagem de sucesso com o status 201 (Created)
            return jsonify({"mensagem":"Livro cadastrado com sucesso"}), 201

# 🔹 Criamos uma rota GET para listar todos os livros cadastrados
@app.route("/livros", methods=["GET"])
def listar_livros():
    # Abrimos a conexão com o banco de dados
    with sqlite3.connect("database.db") as conn:
        # Buscamos todos os registros da tabela LIVROS
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        # Criamos uma lista para guardar os livros formatados em dicionários
        livros_formatados = []

        # Para cada livro encontrado, criamos um dicionário com seus dados
        for item in livros:
           dicionario_livros = {
               "id": item[0],           # ID do livro
               "titulo": item[1],       # Título do livro
               "categoria": item[2],    # Categoria do livro
               "autor": item[3],        # Autor do livro
               "image_url": item[4]     # URL da imagem do livro
           }
           # Adicionamos o dicionário à lista final
           livros_formatados.append(dicionario_livros)

    # Retornamos a lista de livros como JSON com o status 200 (OK)
    return jsonify(livros_formatados), 200

# 🔹 Esse trecho garante que o servidor Flask só será iniciado se esse arquivo for executado diretamente
if __name__ == "__main__":
    # Iniciamos o servidor Flask em modo debug
    # O modo debug ajuda a identificar erros e atualiza a API automaticamente quando o código muda
    app.run(debug=True)