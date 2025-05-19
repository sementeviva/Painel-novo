from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Altere o e-mail e a senha conforme necessário
    novo_usuario = User(nome='Admin', email='admin@admin.com', senha=generate_password_hash('admin123'))
    db.session.add(novo_usuario)
    db.session.commit()
    print("Usuário criado com sucesso!")
