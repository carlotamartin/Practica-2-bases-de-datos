#Este archivo va a tener la configuración de la aplicación
#Flask es una librería de python que se utiliza apra crear aplicaciones web de una manera sencilla

from flask import Flask
from routes.contacts import contacts

#Ahora vamos a importar flask_sqlalchemy porque para concetar nuestra base de datos con la web necesitamos una app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#El config se usa para saber donde nos queremos conectar, este caso en nuestra base de datos que se llama 'contactsdb2', tiene como usuario 'root' y como contraseña 'carlo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:carlo@localhost/contactsdb2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

#Para poder utilizar los blueprints, hay que registrarlos -> register
app.register_blueprint(contacts)