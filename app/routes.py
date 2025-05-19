from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import db, User, Cliente, Conversa
from werkzeug.security import check_password_hash

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return redirect(url_for('main.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.senha, senha):
            session['user_id'] = user.id
            return redirect(url_for('main.dashboard'))
        else:
            flash('Credenciais inválidas. Tente novamente.')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.login'))

@bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    total_clientes = Cliente.query.count()
    total_conversas = Conversa.query.count()
    return render_template('dashboard.html', total_clientes=total_clientes, total_conversas=total_conversas)

@bp.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
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
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
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
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    total_conversas = Conversa.query.count()
    return render_template('estatisticas.html', total_conversas=total_conversas)
@bp.route('/criar_usuario')
def criar_usuario():
    from werkzeug.security import generate_password_hash
    user = User(nome='Admin', email='admin@admin.com', senha=generate_password_hash('admin123'))
    db.session.add(user)
    db.session.commit()
    return "Usuário criado!"
