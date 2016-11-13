from flask import Flask, render_template, url_for, request, redirect, flash
from flask import session
import os, datetime, json, re

app = Flask(__name__)

import dinter

#This function converts a float from range 0 to 1 to a hex code ranging from red to grey to blue.
def indextohex(index):
    r = int(255 * (1-index))
    g = int(255 * index)
    if (g > 128):
        g = 255-g
    b = int(255 * index)
    rhex = format(r,'02x')
    ghex = format(g,'02x')
    bhex = format(b,'02x')
    return(str(rhex)+str(ghex)+str(bhex))

@app.route('/')
def hello_world():

    return redirect("index.html")

@app.route('/q')
def getQuery():
    query = request.args.get('query','')
    data = search(query)
    if(request.args.get('json') != None):
        return jsonify(data)
    else:
         return render_template('q.html',query = query, results=[1,2,3,4])

@app.route('/amalgam')
def getAmalgram():
    query = request.args.get('query','')
    #content = template.getPage(name)
    #return render_template('post.html', post=content['content'], f=globals(), conv=getPython)
    return query

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
