


from flask import Flask, render_template, url_for, request, redirect, flash

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
    search_results = dinter.multi_query(query)
    #print(search_results)
    results_remove=[]
    index = 0
    for result in search_results:
        #print(result["lean"])
        #print(result)
        try:
            result["color"]=indextohex(result["lean"])
            result["text"]=result["text"].replace("sign up for our newsletter","")
            result["blurb"]=result["text"][:300]
            result["title"]=result["text"][:55]
            (result["source"])=getDomain(result["link"])
            if(result["rel"]<0.5):
                results_remove.append(result)
            index += 1
        except:
            print(result)

    for result in results_remove:
        search_results.remove(result)
        #print(result["blurb"])

    return render_template('q.html',query = query, results=(search_results[::-1]))

@app.route('/amalgam')
def getAmalgram():
    query = request.args.get('query','')
    #content = template.getPage(name)
    #return render_template('post.html', post=content['content'], f=globals(), conv=getPython)
    return query

if __name__ == '__main__':
    app.run(port=80, debug=True)
