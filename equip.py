#!/usr/bin/python
print('Content-type: text/html\n')

import cgi
data = cgi.FieldStorage()

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()

import cgitb
cgitb.enable()

def stat_change(stat,value):
    file = open('../www/stats.txt', 'r')
    red = file.read()
    red = red.split('\n')
    red = ' '.join(red)
    red = red.split(' ')
    ind = red.index(stat)
    red.remove(red[ind+1])
    red.insert(ind+1,value)
    coun = 0
    ind = 1
    for x in red:
        if x == '':
            red.remove('')
    lonk = len(red)
    spa = 0
    newl = 0
    spa_turn = 0
    while ((spa + newl) < (lonk - 1)):
        if spa_turn == 0:
            red.insert(ind,' ')
            spa += 1
            spa_turn = 1
        else:
            red.insert(ind,'\n')
            newl += 1
            spa_turn = 0
        ind += 2
    red = ''.join(red)
    file.close()
    file = open('../www/stats.txt', 'w')
    file.write(red)
    file.close()

e = data.getvalue('equip')
w = data.getvalue('web')
def tagger(html, tag, content):
    tag = '</' + tag
    x = html
    lonk = x.find(tag)
    ret = x[:lonk] + content + x[lonk:]
    return(ret)

nor = tagger(s,'head','<link rel="stylesheet" type="text/css" href="reg.css">')
if 'equip' in data:
    if data.getvalue('web') == 'base.py':
        r = open('../www/inventory.txt','w')
    else:
        r = open('../www/inventory.txt','a')
    r.write(e + '\n')
    r.close()
    html = tagger(nor,'body','You equipped ' + e + '!')
    if e == 'Skulmet':
        file = open('../www/stats.txt', 'r')
        red = file.read()
        red = red.split('\n')
        red = ' '.join(red)
        red = red.split(' ')
        ind = red.index('Armor')
        red.remove(red[ind+1])
        red.insert(ind+1,'3')
        coun = 0
        ind = 1
        for x in red:
            if x == '':
                red.remove('')
        lonk = len(red)
        spa = 0
        newl = 0
        spa_turn = 0
        while ((spa + newl) < (lonk - 1)):
            if spa_turn == 0:
                red.insert(ind,' ')
                spa += 1
                spa_turn = 1
            else:
                red.insert(ind,'\n')
                newl += 1
                spa_turn = 0
            ind += 2
        red = ''.join(red)
        file.close()
        file = open('../www/stats.txt', 'w')
        file.write(red)
        file.close()
    elif e == "Firesword":
        stat_change('Attack','6')
    print(tagger(html,'body','<a href="'+ w +'"> Proceed </a>'))
else:
    print(tagger(nor,'body','These are not the droids you are looking for.'))
