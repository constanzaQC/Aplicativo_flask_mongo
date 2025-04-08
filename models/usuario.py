from mongoengine import *


class Usuario(Document):
    usuario = StringField(unique=True, required=True, max_length=50)
    password = StringField(required=True, max_length=50)  
    nombres = StringField(required=True, max_length=50)
    apellidos = StringField(required=True, max_length=50)
    correo = EmailField(unique=True, required=True)

    def __repr__(self):
        return f"{self.nombres} {self.apellidos}"
