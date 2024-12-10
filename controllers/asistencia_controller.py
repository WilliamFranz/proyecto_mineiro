from  flask import request,redirect,url_for,Blueprint

from models.asistencia_model import Asistencia
from views import asistencia_view

asistencia_bp = Blueprint('asistencia',__name__,url_prefix="/asistencias")

@asistencia_bp.route("/")
def index():
    #recupera todos los registros
    asistencias = Asistencia.get_all()
    return asistencia_view.list(asistencias)

@asistencia_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        hora = request.form['hora']
        movil = request.form['movil']
        fecha = request.form['fecha']
        
        asistencia = Asistencia(nombre,hora,movil,fecha)
        asistencia.save()
        return redirect(url_for('asistencia.index'))
        
    return asistencia_view.create()

@asistencia_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    asistencia = Asistencia.get_by_id(id)
    if request.method == 'POST':
        nombre =  request.form['nombre']
        hora =  request.form['hora']
        movil =  request.form['movil']
        fecha =  request.form['fecha']
        
        asistencia.update(nombre=nombre,hora=hora,movil=movil,fecha=fecha)
        return redirect(url_for('asistencia.index'))
        
    return asistencia_view.edit(asistencia)

@asistencia_bp.route("/delete/<int:id>")
def delete(id):
    asistencia = Asistencia.get_by_id(id)
    asistencia.delete()
    return redirect(url_for('asistencia.index'))

