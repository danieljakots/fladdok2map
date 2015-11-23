#!/usr/bin/env python3.4

from flask import render_template, request, redirect, url_for, Blueprint
import addok2map

fladdok2map = Blueprint('fladdok2map', __name__, url_prefix='/addok2map',
                        template_folder='templates')

@fladdok2map.route('/apropos')
def apropos():
    return render_template('apropos.html')

@fladdok2map.route('/')
def recherche():
    return render_template('recherche.html')

@fladdok2map.route('/resultats', methods=['GET', 'POST'])
def resultats():
    if request.method == 'POST':
        results = addok2map.lookup(request.form['address'])
        return render_template('resultats.html', entries=results)

    else:
        return redirect(url_for('fladdok2map.apropos'))

