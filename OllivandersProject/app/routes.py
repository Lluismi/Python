from flask import Flask, render_template
from . import app
from main import stock

@app.route('/')
@app.route('/frontend/index.html')
def frontend():
    return render_template('frontend/index.html') 

@app.route('/frontend/agedbrie.html')
def AgedBrie():
    return render_template('frontend/agedbrie.html') 

@app.route('/frontend/backstagepass.html')
def BackStagePass():
    return render_template('frontend/backstagepass.html') 

@app.route('/frontend/conjured.html')
def Conjured():
    return render_template('frontend/conjured.html') 

@app.route('/frontend/normalitem.html')
def NormalItem():
    return render_template('frontend/normalitem.html')

@app.route('/frontend/sulfuras.html')
def Sulfuras():
    return render_template('frontend/sulfuras.html')

@app.route('/backend/index.html')
def backend():
    return render_template('backend/index.html')
    
@app.route('/backend/modificar.html')
def modificar_objeto():
    return render_template('backend/modificar.html')

@app.route('/backend/insertar.html')
def insertar_objeto():
    return render_template('backend/insertar.html')

@app.route('/backend/añadirdia.html')
def añadir_dia():
    return render_template('backend/añadirdia.html')

@app.route('/get_items')
def get_items():
    return '<p>{}</p>'.format(stock.get_items())

@app.route('/frontend/getitems.html')
def update_quality():
    return render_template('backend/getitems.html', items=update_quality())
