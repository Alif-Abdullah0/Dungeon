#!/usr/bin/python
print('Content-type: text/html\n')

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()

def formboi(file,select_name,option_value,option_name,file_ret_name=''):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    html += '<select name="' + select_name + '"> \n'
    for x in option_value:
        ind = option_value.index(x)
        html += '<option value="' + x + '">' + option_name[ind] + '</option> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)

def tagger(html, tag, content):
    tag = '</' + tag
    x = html
    lonk = x.find(tag)
    ret = x[:lonk] + content + x[lonk:]
    return(ret)
html = tagger(s, 'head', "<style> body{color:orange;text-align:center;background-color:rgb(251, 255, 212);} .topnav {overflow: hidden;background-color: rgb(255,165,0);} .topnav a {float: left;color: rgb(242,242,242);text-align: center;padding: 14px 16px;text-decoration: none;font-size: 17px;} .topnav a:hover {background-color: rgb(221,0,221);color: black;} .topnav a.active {background-color: rgb(76, 175, 80);color: white;}</style>")

noug = tagger(html,'body','<div class ="topnav"> <a href="entry.py"> View our game! </a> <a href="credit.py"> Sites that helped us make this! </a> </div>')

heading = tagger(noug,'body','<h2> Welcome to our Shop! </h2> \n')

text = tagger(heading,'body','Hi there traveller! If you are seeing this, this is a work in progress, but at least it is visible!')

print(text)

