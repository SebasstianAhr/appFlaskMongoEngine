from mongoengine import Document, ReferenceField, StringField, IntField, EmailField
#Crear la clase que representa la colección usuario en la base de datos
class Usuario (Document):
    usuario = StringField(max_length=50, required=True, unique=True)
    password = StringField(max_length=50)
    nombres = StringField(max_length=50)
    apellidos = StringField(max_length=50)
    correo = EmailField(required=True, unique=True)
#Crear clase que representa la colección categoria en la base de datos
class Categoria (Document):
    nombre=StringField(max_length=50, unique=True)
#crear la clase que representa la colección producto en la base de datos
class Producto(Document):
    codigo = IntField(unique=True)
    nombre = StringField(max_length=50)
    precio =IntField()
    categoria = ReferenceField (Categoria)

