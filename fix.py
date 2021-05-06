#!/usr/bin/python
print('Content-type: text/html\n')

import random

import cgitb
cgitb.enable()

import cgi
data = cgi.FieldStorage()

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()
#sel_name and file in strings
def formboi(file,select_name,option_value,option_name):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    html += '<select name="' + select_name + '"> \n'
    for x in option_value:
        ind = option_value.index(x)
        html += '<option value="' + x + '">' + option_name[ind] + '</option> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)
print(formboi('foo.py', 'what', ['o1','o2'],['this', 'that']))

def formtext(file,name,preface=''):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    if not(preface==''):
        html += preface + ' \n '
    html += '<input type="text" name="' + name + '"> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)

def tagger(html, tag, content):
    tag = '</' + tag
    x = html
    lonk = x.find(tag)
    ret = x[:lonk] + content + x[lonk:]
    return(ret)

def inventory_wipe():
    r = open('../www/inventory.txt','w')
    r.close()
    
def stat_reset():
    stat_change('HP','20')
    stat_change('GP','0')
    stat_change('Armor','2')
    stat_change('Attack','3')
    
inventory_wipe()
stat_reset()

print(tagger(s,'body','Should be all fixed! <a href="entry.py"> Return </a>'))
