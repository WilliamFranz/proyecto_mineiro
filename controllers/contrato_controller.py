from  flask import request,redirect,url_for,Blueprint

from models.contrato_model import Contrato

from views import contrato_view

contrato_bp = Blueprint('contrato',__name__,url_prefix="/contratos")

@contrato_bp.route("/")
def index():
    #recupera todos los registros
    contratos = Contrato.get_all()
    return contrato_view.list(contratos)

@contrato_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        empresa = request.form['empresa']
        nombre_cliente = request.form['nombre_cliente']
        origen = request.form['origen']
        destino_final = request.form['destino_final']
        precio_servicio = request.form['precio_servicio']
        nombre_conductor = request.form['nombre_conductor']
        numero_movil = request.form['numero_movil']
        fecha = request.form['fecha']
        
        contrato = Contrato(empresa,nombre_cliente,origen,destino_final,precio_servicio,nombre_conductor,numero_movil,fecha)
        contrato.save()
        return redirect(url_for('contrato.index'))
        
    return contrato_view.create()

@contrato_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    contrato = Contrato.get_by_id(id)
    if request.method == 'POST':
        empresa =  request.form['empresa']
        nombre_cliente =  request.form['nombre_cliente']
        origen =  request.form['origen']
        destino_final =  request.form['destino_final']
        precio_servicio =  request.form['precio_servicio']
        nombre_conductor=  request.form['nombre_conductor']
        numero_movil=  request.form['numero_movil']
        fecha =  request.form['fecha']
        
        contrato.update(empresa=empresa,nombre_cliente=nombre_cliente,origen=origen,destino_final=destino_final,precio_servicio=precio_servicio,nombre_conductor=nombre_conductor,numero_movil=numero_movil,fecha=fecha)
        return redirect(url_for('contrato.index'))
        
    return contrato_view.edit(contrato)

@contrato_bp.route("/delete/<int:id>")
def delete(id):
    contrato = Contrato.get_by_id(id)
    contrato.delete()
    return redirect(url_for('contrato.index'))

