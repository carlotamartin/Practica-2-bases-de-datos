#Esta carpeta va a contener los datos que queremos de casa usuario
from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True) #El ID va a ser entero y único
    #Van a ser cadenas de texto que tienen como maximo 100 carácteres
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

#Cremos el constructor
    def __init__(self, fullname, email, phone) :
        self.email = email
        self.fullname = fullname
        self.phone = phone
