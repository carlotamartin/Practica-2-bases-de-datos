#En este archivo, vamos a tener todas las rutas de una forma organizada
#Blueprint -> son los módulos con los que se construye la aplicación, su objetivo es la organización del códio
#render_template -> es un módulo que sirva para distribuit un archivo html al navegador
#request -> se utiliza para leer los datos introducidos en el formulario
from flask import Blueprint, render_template, request

#Importamos el constructor de un contacto
from models.contact import Contact

#Importamos la clase db, para realizar la conexión con la base de datos
from utils.db import db

contacts = Blueprint ('contacts', __name__)

#En las rutas, se pueden devolver tanto un string como un html
@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new', methods= ['POST'])
def add_contact():
    #Guardamos cada dato del ['POST'] en cada variable
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    #Ahora con estos datos, creamos un contacto nuevo
    new_contact = Contact(fullname, email, phone)

    #Guardamos el contacto en la base de datos
    db.session.add(new_contact)
    db.session.commit()
    return 'saving a contact'

#Crearemos esta ruta para cuando la aplicación añada un contacto
@contacts.route('/update')
def update_contact():
    return 'update a contact'

#Crearemos esta ruta para cuando la aplicación elimine un contacto
@contacts.route('/delete')
def delete_contact():
    return 'delete a contact'

@contacts.route('/abaut')
def abaut():
    return render_template('abaut.html')
