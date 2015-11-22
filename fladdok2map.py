#!/usr/bin/env python3.4

from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import addok2map

app = Flask(__name__)

@app.route('/apropos')
def apropos():
    return render_template('apropos.html')

@app.route('/')
def recherche():
    return render_template('recherche.html')

@app.route('/resultats', methods=['GET', 'POST'])
def resultats():
    if request.method == 'POST':
        results = addok2map.lookup(request.form['address'])
        return render_template('resultats.html', entries=results)

    else:
        return redirect(url_for('apropos'))

@app.route('/test')
def test():
    return redirect(url_for('apropos'))

if __name__ == '__main__':
    app.debug = False
    app.run()
