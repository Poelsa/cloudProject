from flask import render_template, flash, redirect, jsonify, request
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/led')
def led():
    return render_template('led_config.html')

@app.route('/led_config', methods=['POST'])
def light_led():
    #Get values from form, and do the dotstar script
    return jsonify({
        'index': request.form['index']
        })
