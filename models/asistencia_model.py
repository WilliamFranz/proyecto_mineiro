from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Asistencia(db.Model):
    __tablename__ = "asistencias"
    
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    hora = db.Column(db.String(20),nullable=False)
    movil = db.Column(db.String,nullable=False)
    fecha = db.Column(db.String(20),nullable=False)
    
    def __init__(self, nombre, hora, movil, fecha):
        self.nombre = nombre
        self.hora = hora 
        self.movil = self.hash_movil(movil) 
        self.fecha = fecha 
    
    @staticmethod    
    def hash_movil(movil):
      return generate_password_hash(movil)
    
    def verify_movil(self,movil):
       return check_password_hash(self.movil, movil)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod    
    def get_all():
        return Asistencia.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Asistencia.query.get(id)
    
    def update(self,nombre=None,hora=None,movil=None,fecha=None):
        if nombre:
            self.nombre = nombre
        if hora:
            self.hora = hora
        if movil:
            self.movil = movil
        if fecha:
            self.fecha = fecha
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        