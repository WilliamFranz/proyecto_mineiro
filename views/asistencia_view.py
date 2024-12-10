from flask import render_template

def list(asistencias):
    return render_template('asistencias/index.html', asistencias=asistencias)

def create():
    return render_template('asistencias/create.html')

def edit(asistencia):
    return render_template('asistencias/edit.html',asistencia=asistencia)