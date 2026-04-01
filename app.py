from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro/cliente')
def cadastro_cliente():
    return render_template('contratante.html')

@app.route('/cadastro/freelancer')
def cadastro_freelancer():
    return render_template('profissional.html')


if __name__ == '__main__':
    app.run(debug=True)
