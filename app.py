from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"]= "Cualquier cosa"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/flask_bootstrap'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Message(db.Model):
  __tablename__ = 'messages'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f'<Message {self.title}>'
    
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
        if not title:
            flash("El titulo es obligatorio")
        elif not content:
            flash("El contenido es obligatorio")    
        else:
            messages.append({"title": title,"content": content})
            return redirect(url_for("index"))

    return render_template('create.html')
    
@app.route('/usuario/<name>')
def user(name):
  return render_template('user.html', name = name)

@app.route('/usuario')
def stranger():
  return render_template('user.html')


@app.route('/navegador')
def browser():
  user_agent = request.headers.get('User-Agent')
  return f'Tu navegafor es: {user_agent}'

@app.route('/rutas')
def routes():
  
  print(app.url_map)
  return 'revisa tu consola para ver las rutas'

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 400














