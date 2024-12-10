from flask import render_template

def list(contratos):
    return render_template('contratos/index.html', contratos=contratos)

def create():
    return render_template('contratos/create.html')

def edit(contrato):
    return render_template('contratos/edit.html',contrato=contrato)