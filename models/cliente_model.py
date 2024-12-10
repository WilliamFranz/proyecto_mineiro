from database import db

class Cliente(db.Model):
    __tablename__ = "clientes"
    
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    numero = db.Column(db.String(20),nullable=False)
    familia = db.Column(db.String(50),nullable=False)
    hora = db.Column(db.String(20),nullable=False)
    movil = db.Column(db.String(20),nullable=False)
    fecha = db.Column(db.String(20),nullable=False)
    
    def __init__(self, nombre, numero, familia, hora, movil, fecha):
        self.nombre = nombre
        self.numero = numero
        self.familia = familia
        self.hora = hora
        self.movil = movil
        self.fecha = fecha
     
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod    
    def get_all():
        return Cliente.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Cliente.query.get(id)
    
    def update(self,nombre=None,numero=None,familia=None,hora=None,movil=None,fecha=None):
        if nombre and numero and familia and hora and movil and fecha:
            self.nombre = nombre
            self.numero = numero
            self.familia = familia
            self.hora = hora
            self.movil = movil
            self.fecha = fecha
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        