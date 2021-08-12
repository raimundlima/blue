from flask import Flask, render_template, redirect, request, flash ,session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key='room3'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///room3.sqlite3'

# app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://choeciam:ym0KPzAmu9bPMiypkoUyTf58hIhjE2fZ@kesavan.db.elephantsql.com/choeciam'

db = SQLAlchemy(app)


class Guitar(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(300),nullable=False)
    imagem = db.Column(db.String(500),nullable=False)
    descricao = db.Column(db.String(600),nullable=False)

    def __init__(self,nome,imagem,descricao):
        self.nome = nome
        self.imagem = imagem
        self.descricao = descricao


#Rota Principal

@app.route ('/')
def index():
    return render_template('index.html')


#rota catalogo
@app.route ('/catalogo')
def catalogo():
    guitar = Guitar.query.all()
    return render_template ('catalogo.html', guitar = guitar )

@app.route ('/adm')
def adm():
    guitars = Guitar.query.all()
    return render_template ('adm.html', guitars = guitars )

#Rota Login 

@app.route('/login')
def login():
    session['usuario_logado'] = None
    return render_template('login.html')

#Rota de autenticação

@app.route('/auth',methods=['GET','POST'])
def auth ():
    if request.form['senha'] == '1234':
       session ['usuario_logado'] = '1234'
       flash('Login feito com sucesso!')
       return redirect('/adm')
    else:
        flash('erro no login, tente novamente!')
        return redirect ('/login')

# Rota para logout
@app.route('/logout')
def logout ():
    session ['usuario_logado'] = None
    return redirect ('/login')


@app.route('/add', methods=['GET','POST'])
def add():
    if request.method =='POST':
        guitar = Guitar (
            request.form['nome'],
            request.form['imagem'],
            request.form['descricao']
            )
        db.session.add(guitar)
        db.session.commit()
        return redirect('/catalogo')

@app.route('/edit/<id>',methods=['GET','POST'])
def edit (id):
    guitar = Guitar.query.get(id)
    guitars = Guitar.query.all()
    if request.method =='POST':
        guitar.nome = request.form['nome']
        guitar.imagem = request.form['imagem']
        guitar.descricao = request.form['descricao']
        db.session.commit()
        return redirect ('/adm')
    return render_template('adm.html',guitar=guitar, guitars=guitars)

@app.route('/<id>')
def get_by_id(id):
    guitar = Guitar.query.get(id)
    all = Guitar.query.all()
    return render_template('adm.html', guitarDelete = guitar, guitars =all)

@app.route('/delete/<id>')
def delete(id):
    guitar=Guitar.query.get(id)
    db.session.delete(guitar)
    db.session.commit()
    return redirect('/adm')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    