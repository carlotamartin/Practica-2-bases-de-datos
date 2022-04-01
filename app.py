#Este archivo va a tener la configuración de la aplicación
#Flask es una librería de python que se utiliza apra crear aplicaciones web de una manera sencilla

from flask import Flask
from routes.contacts import contacts

#Ahora vamos a importar flask_sqlalchemy porque para concetar nuestra base de datos con la web necesitamos una app
from flask_sqlalchemy import SQLAlchemy

from config import DATABASE_CONNECTION_URI
app = Flask(__name__)

app.secret_key = 'mysecret'
print(DATABASE_CONNECTION_URI)
#El config se usa para saber donde nos queremos conectar, este caso en nuestra base de datos que se llama 'contactsdb', tiene como usuario 'root' y como contraseña 'carlo'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

#Para poder utilizar los blueprints, hay que registrarlos -> register
app.register_blueprint(contacts)