import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS LIVROS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            autor TEXT NOT NULL,
            image_url TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET"])
def index():
    return "<h1>API de Livros</h1><p>Bem-vindo à nossa API de livros!</p>"

@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()
    if isinstance(dados, list):
        resultados = []
        for livro in dados:
            titulo = livro.get("titulo")
            categoria = livro.get("categoria")
            autor = livro.get("autor")
            image_url = livro.get("image_url")
            if not titulo or not categoria or not autor or not image_url:
                return jsonify({"Erro": "Todos os campos são obrigatórios"}), 400
            conn = get_db_connection()
            conn.execute("""
                INSERT INTO LIVROS (titulo, categoria, autor, image_url)
                VALUES (?, ?, ?, ?)
            """, (titulo, categoria, autor, image_url))
            conn.commit()
            conn.close()
            resultados.append({"titulo": titulo, "status": "cadastrado com sucesso"})
        return jsonify({"mensagem": "Livros cadastrados com sucesso", "resultados": resultados}), 201
    else:
        titulo = dados.get("titulo")
        categoria = dados.get("categoria")
        autor = dados.get("autor")
        image_url = dados.get("image_url")
        if not titulo or not categoria or not autor or not image_url:
            return jsonify({"Erro": "Todos os campos são obrigatórios"}), 400
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO LIVROS (titulo, categoria, autor, image_url)
            VALUES (?, ?, ?, ?)
        """, (titulo, categoria, autor, image_url))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

@app.route("/livros", methods=["GET"])
def listar_livros():
    conn = get_db_connection()
    livros = conn.execute("SELECT * FROM LIVROS").fetchall()
    conn.close()
    livros_formatados = [{"id": livro["id"], "titulo": livro["titulo"], "categoria": livro["categoria"], "autor": livro["autor"], "image_url": livro["image_url"]} for livro in livros]
    return jsonify(livros_formatados), 200

if __name__ == "__main__":
    app.run(debug=True)