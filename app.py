from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'chave-secreta'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = User(
            nome=request.form['nome'],
            email=request.form['email'],
            profissao=request.form['profissao'],
            valor=request.form['valor'],
            descricao=request.form['descricao']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('freelancers'))

    return render_template('cadastro.html')

@app.route('/freelancers')
def freelancers():
    usuarios = User.query.all()
    return render_template('freelancers.html', usuarios=usuarios)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
