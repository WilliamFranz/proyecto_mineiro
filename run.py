from flask import Flask, render_template, request, redirect, url_for, flash, session

from controllers import asistencia_controller, cliente_controller, contrato_controller

from database import db

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
USERS = {
    'admin': 'password123',
    'ADMINISTRADOR': '1234'
}

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mineiro.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(asistencia_controller.asistencia_bp)
app.register_blueprint(cliente_controller.cliente_bp)
app.register_blueprint(contrato_controller.contrato_bp)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USERS and USERS[username] == password:
            session['username'] = username 
            return redirect(url_for('welcome'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login')) 
    return render_template('welcome.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None) 
    flash('Sesión cerrada con éxito', 'info')
    return redirect(url_for('login'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)