import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SECRET_KEY'] = 'segredo-super-seguro'

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        senha_hash = generate_password_hash(request.form['senha'])

        user = User(
            nome=request.form['nome'],
            email=request.form['email'],
            senha=senha_hash,
            tipo=request.form['tipo'],
            profissao=request.form.get('profissao'),
            valor=request.form.get('valor'),
            descricao=request.form.get('descricao')
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/freelancers')
def freelancers():
    usuarios = User.query.all()
    return render_template('freelancers.html', usuarios=usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()

        if user and check_password_hash(user.senha, request.form['senha']):
            session['user_id'] = user.id
            session['tipo'] = user.tipo
            session['nome'] = user.nome

            if user.tipo == 'contratante':
                return redirect(url_for('area_contratante'))
            else:
                return redirect(url_for('area_profissional'))

        return render_template('login.html', error='Email ou senha inválidos')

    return render_template('login.html')

@app.route('/contratante')
def area_contratante():
    if session.get('tipo') != 'contratante':
        return redirect(url_for('login'))

    profissionais = User.query.filter_by(tipo='profissional').all()
    return render_template('contratante.html', profissionais=profissionais)

@app.route('/profissional')
def area_profissional():
    if session.get('tipo') != 'profissional':
        return redirect(url_for('login'))

    return render_template('profissional.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
