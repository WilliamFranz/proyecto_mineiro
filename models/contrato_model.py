from database import db

class Contrato(db.Model):
    __tablename__ = "contratos"
    
    id = db.Column(db.Integer,primary_key=True)
    empresa = db.Column(db.String(80),nullable=False)
    nombre_cliente = db.Column(db.String(80),nullable=False)
    origen = db.Column(db.String(20),nullable=False)
    destino_final = db.Column(db.String(50),nullable=False)
    precio_servicio = db.Column(db.String(20),nullable=False)
    nombre_conductor = db.Column(db.String(20),nullable=False)
    numero_movil = db.Column(db.String(20),nullable=False)
    fecha = db.Column(db.String(20),nullable=False)
    
    def __init__(self, empresa, nombre_cliente, origen, destino_final, precio_servicio, nombre_conductor, numero_movil, fecha):
        self.empresa = empresa
        self.nombre_cliente = nombre_cliente
        self.origen = origen
        self.destino_final = destino_final
        self.precio_servicio = precio_servicio
        self.nombre_conductor = nombre_conductor
        self.numero_movil = numero_movil
        self.fecha = fecha
     
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod    
    def get_all():
        return Contrato.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Contrato.query.get(id)
    
    def update(self,empresa=None,nombre_cliente=None,origen=None,destino_final=None,precio_servicio=None,nombre_conductor=None,numero_movil=None,fecha=None):
        if empresa and nombre_cliente and origen and destino_final and precio_servicio and nombre_conductor and numero_movil and fecha:
            self.empresa = empresa
            self.nombre_cliente = nombre_cliente
            self.origen = origen
            self.destino_final = destino_final
            self.precio_servicio = precio_servicio
            self.nombre_conductor = nombre_conductor
            self.numero_movil = numero_movil
            self.fecha = fecha
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        