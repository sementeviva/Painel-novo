from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, User, Cliente, Conversa

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return redirect(url_for('main.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('main.dashboard'))
    return render_template('login.html')

@bp.route('/dashboard')
def dashboard():
    total_clientes = Cliente.query.count()
    total_conversas = Conversa.query.count()
    return render_template('dashboard.html', total_clientes=total_clientes, total_conversas=total_conversas)

@bp.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        cliente = Cliente(nome=nome, telefone=telefone)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('cadastrar_cliente.html')

@bp.route('/treinar_bot', methods=['GET', 'POST'])
def treinar_bot():
    if request.method == 'POST':
        pergunta = request.form['pergunta']
        resposta = request.form['resposta']
        conversa = Conversa(mensagem=pergunta, resposta=resposta)
        db.session.add(conversa)
        db.session.commit()
        return redirect(url_for('main.treinar_bot'))
    return render_template('treinar_bot.html')

@bp.route('/estatisticas')
def estatisticas():
    total_conversas = Conversa.query.count()
    return render_template('estatisticas.html', total_conversas=total_conversas)