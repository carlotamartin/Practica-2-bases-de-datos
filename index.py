#Este archivo se va a utilizar para que la aplicación empiece a funcionar
from app import app
from utils.db import db

#Con esta función, va a crear las tablas que hemos definido en contact.py
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    #debug=True se utiliza para que la consola no tengamos que reiniciar cada vez que cambiamos el código
    app.run(debug=True, host='0.0.0.0')