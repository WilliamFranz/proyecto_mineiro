from  flask import request,redirect,url_for,Blueprint

from models.cliente_model import Cliente

from views import cliente_view

cliente_bp = Blueprint('cliente',__name__,url_prefix="/clientes")

@cliente_bp.route("/")
def index():
    #recupera todos los registros
    clientes = Cliente.get_all()
    return cliente_view.list(clientes)

@cliente_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        numero = request.form['numero']
        familia = request.form['familia']
        hora = request.form['hora']
        movil = request.form['movil']
        fecha = request.form['fecha']
        
        cliente = Cliente(nombre,numero,familia,hora,movil,fecha)
        cliente.save()
        return redirect(url_for('cliente.index'))
        
    return cliente_view.create()

@cliente_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    cliente = Cliente.get_by_id(id)
    if request.method == 'POST':
        nombre =  request.form['nombre']
        numero =  request.form['numero']
        familia =  request.form['familia']
        hora =  request.form['hora']
        movil =  request.form['movil']
        fecha =  request.form['fecha']
        
        cliente.update(nombre=nombre,numero=numero,familia=familia,hora=hora,movil=movil,fecha=fecha)
        return redirect(url_for('cliente.index'))
        
    return cliente_view.edit(cliente)

@cliente_bp.route("/delete/<int:id>")
def delete(id):
    cliente = Cliente.get_by_id(id)
    cliente.delete()
    return redirect(url_for('cliente.index'))

