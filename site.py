from flask import Flask, render_template, url_for, request, redirect, flash
from flask import session
import os, datetime, json, re




#test

app = Flask(__name__)


pageLocation = os.path.join(os.path.abspath(os.path.join(app.static_folder, '..')), 'pages')
import template

from backends import dyn
app.secret_key= os.urandom(24)

app.register_blueprint(dyn, url_prefix='/dyn')

@app.route('/')
def hello_world():

    return render_template('landing.html', f=globals(), conv=getPython)

@app.route('/q>')
def getQuery(name):
    query = request.args.get('query','')
    #content = template.getPage(name)
    #return render_template('post.html', post=content['content'], f=globals(), conv=getPython)
    return query

@app.route('/amalgam')
def getAmalgram(name):
    query = request.args.get('query,'')
    #content = template.getPage(name)
    #return render_template('post.html', post=content['content'], f=globals(), conv=getPython)
    return query

if __name__ == '__main__':
    app.run(debug=True)
