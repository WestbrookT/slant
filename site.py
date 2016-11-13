from flask import Flask, render_template, url_for, request, redirect, flash
from flask import session
import os, datetime, json, re

app = Flask(__name__)

import dinter

def getDomain(url):
    pat = r'((https?):\/\/)?(\w+\.)*(?P<domain>\w+)\.(\w+)(\/.*)?'
    m = re.match(pat, url)
    if m:
        domain = m.group('domain')
        return domain
    else:
        return False

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
    print("Hiiiii I'm doing a search lol")
    search_results = dinter.lambda_query(query)
    #print(search_results)
    results_remove=[]
    for result in search_results:
        #print(search_results[result]["lean"])


        search_results[result]["color"]=indextohex(search_results[result]["lean"])
        search_results[result]["text"]=search_results[result]["text"].replace("sign up for our newsletter","")
        search_results[result]["blurb"]=search_results[result]["text"][:300]
        search_results[result]["title"]=search_results[result]["text"][:55]
        (search_results[result]["source"])=getDomain(result)
        if(search_results[result]["rel"]<0.5):
            results_remove.append(result)

    for result in results_remove:
        search_results.pop(result, None)
        #print(search_results[result]["blurb"])
    return render_template('q.html',query = query, results=(search_results))

@app.route('/amalgam')
def getAmalgram():
    query = request.args.get('query','')
    #content = template.getPage(name)
    #return render_template('post.html', post=content['content'], f=globals(), conv=getPython)
    return query

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=80, debug=True)
