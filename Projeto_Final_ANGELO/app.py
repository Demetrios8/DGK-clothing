from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'segredo-super-seguro'  # necessário para usar sessão

# Produtos simulados
produtos = [
    {"id": 1, "nome": "Camiseta Street", "preco": 79.90},
    {"id": 2, "nome": "Moletom Oversized", "preco": 149.90},
    {"id": 3, "nome": "Boné Snapback", "preco": 59.90}
]

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/adicionar/<int:id>')
def adicionar(id):
    if 'carrinho' not in session:
        session['carrinho'] = []
    session['carrinho'].append(id)
    session.modified = True
    return redirect(url_for('index'))

@app.route('/remover/<int:id>')
def remover(id):
    if 'carrinho' in session:
        session['carrinho'] = [i for i in session['carrinho'] if i != id]
        session.modified = True
    return redirect(url_for('carrinho'))

@app.route('/limpar')
def limpar():
    session.pop('carrinho', None)
    return redirect(url_for('carrinho'))

@app.route('/carrinho')
def carrinho():
    itens = []
    total = 0
    if 'carrinho' in session:
        for id in session['carrinho']:
            produto = next((p for p in produtos if p["id"] == id), None)
            if produto:
                itens.append(produto)
                total += produto["preco"]
    return render_template('carrinho.html', itens=itens, total=total)

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensagem = ""
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == "admin" and senha == "123":
            mensagem = "Login bem-sucedido!"
        else:
            mensagem = "Usuário ou senha incorretos."
    return render_template('login.html', mensagem=mensagem)

if __name__ == '__main
