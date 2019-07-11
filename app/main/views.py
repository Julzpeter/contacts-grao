from flask import render_template,request,redirect,url_for,abort
from . import main

# Views
@main.route('/contacts/')
def contacts():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('contacts.html', title = title )

# @main.route('/contact')
# def contact():
#     return render_template('index.html')