from flask import Flask, render_template, url_for, request, redirect, flash
from flask import session
import os, datetime, json, re

app = Flask(__name__)

#import dinter

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
    return render_template('homesearch.html')

@app.route('/q')
def getQuery():
    query = request.args.get('query','')
    return render_template('q.html',query = query, results=[{"color":indextohex(0.2),"title":"Donald Trump Eats The Best Poop","blurb":"Donald Trump eats only the best poop","link":"http://breitbart.com","source":"Breitbart","image":"http://i.imgur.com/q73B2jL.jpg"},{"color":indextohex(0.9),"title":"Donald Trump Eats The Worst Poop","blurb":"Donald Trump eats only the worst poop","link":"http://buzzfeed.com","source":"Buzzfeed","image":"http://i.imgur.com/gPceg2V.jpg"},{"color":indextohex(0.55),"title":"The Case For Eating Poop Like Trump","blurb":"Donald Trump has a good reason to eat poop and so do you","link":"http://breitbart.com","source":"The Atlantic","image":"http://i.imgur.com/q73B2jL.jpg"},{"color":indextohex(0.75),"title":"Eating poop does not represent America","blurb":"We must not allow the practice of eating poop to be acceptable in the nation","link":"http://buzzfeed.com","source":"Everyday Feminism","image":"http://i.imgur.com/gPceg2V.jpg"},{"color":indextohex(0.50),"title":"The history of eating poop in America","blurb":"This nation has had a long history with people who secretly eat poop","link":"http://buzzfeed.com","source":"Washington Post","image":"http://i.imgur.com/gPceg2V.jpg"}])

@app.route('/amalgam')
def getAmalgram():
    query = request.args.get('query','')
    #content = template.getPage(name)
    #return render_template('post.html', post=content['content'], f=globals(), conv=getPython)
    return query

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
