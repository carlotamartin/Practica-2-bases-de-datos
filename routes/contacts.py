#En este archivo, vamos a tener todas las rutas de una forma organizada
#Blueprint -> son los módulos con los que se construye la aplicación, su objetivo es la organización del códio
#render_template -> es un módulo que sirva para distribuit un archivo html al navegador
#request -> se utiliza para leer los datos introducidos en el formulario
#redirect-> te redirecciona a otras secciones
#url_for -> para redireccionar a alguna lado
#flask-> para alertas
from flask import Blueprint, render_template, request, redirect, url_for, flash

#Importamos el constructor de un contacto
from models.contact import Contact

#Importamos la clase db, para realizar la conexión con la base de datos
from utils.db import db

contacts = Blueprint ('contacts', __name__)

#En las rutas, se pueden devolver tanto un string como un html
@contacts.route('/')
def index():
    #Query se utiliza para 'traer' todos los datos que están en la tabla
    contacts = Contact.query.all() #lista de todos los contactos
    return render_template('index.html', contacts = contacts) #le mostramos la lista de todos los contactos para poder listarla

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

    flash('¡Has añadido un nuevo contacto!')
    return redirect(url_for('contacts.index'))

#Crearemos esta ruta para cuando la aplicación añada un contacto
@contacts.route('/update_contact/<id>', methods=['POST', 'GET'])
def update_contact(id):
    contact = Contact.query.get(id)
    #aqui lo que queremos es actualizar los datos en la base de datos
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('¡Se han modificado los datos del contacto!')

        return redirect(url_for('contacts.index'))
    return render_template('update_contact.html', contact=contact)

#Crearemos esta ruta para cuando la aplicación elimine un contacto
@contacts.route('/delete/<id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('¡Contacto eliminado!')
    #Cuando eliminemos un contacto que se redirija a la página inicial
    return redirect(url_for('contacts.index'))

#Estas dos rutas las he creado como ejemplo pero no contienen nada importante
@contacts.route('/about')
def about():
    return render_template('about.html')

@contacts.route('/info')
def info():
    return render_template('info.html')

