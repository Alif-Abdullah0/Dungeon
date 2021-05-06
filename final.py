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

def tagger(html, tag, content):
    tag = '</' + tag
    x = html
    lonk = x.find(tag)
    ret = x[:lonk] + content + x[lonk:]
    return(ret)
html = (tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='door.css'>"))

es = open("../www/names.txt")
lis = es.read()
es.close()

Monarchs = tagger(html,'body','Here is a list of all the monarchs who have come before you. <br> Comic <br>' + lis)
print(Monarchs)