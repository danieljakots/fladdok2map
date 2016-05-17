#!/usr/bin/env python3.4

#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004

# Copyright (C) 2015, 2016 Daniel Jakots <vigdis@chown.me>

# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

# 0. You just DO WHAT THE FUCK YOU WANT TO.
#

from flask import Flask, render_template, request, redirect, url_for
from fladdok2map import addok2map

application = Flask(__name__)

@application.route('/apropos')
def apropos():
    return render_template('apropos.html')

@application.route('/')
def recherche():
    return render_template('recherche.html')

@application.route('/resultats', methods=['GET', 'POST'])
def resultats():
    if request.method == 'POST':
        if request.form['address']:
            results = addok2map.lookup(request.form['address'])
            return render_template('resultats.html', entries=results)
        else:
            return redirect(request.url_root)

    else:
        return redirect(request.url_root)


def main():
    application.debug = False
    application.run()


if __name__ == '__main__':
    main()
