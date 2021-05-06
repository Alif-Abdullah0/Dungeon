#!/usr/bin/python

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()

print('Content-type: text/html\n')

import cgitb
cgitb.enable()

def tagger(html, tag, content):
    tag = '</' + tag
    x = html
    lonk = x.find(tag)
    ret = x[:lonk] + content + x[lonk:]
    return(ret)

def inventory_wipe():
    r = open('../www/inventory.txt','w')
    r.close()

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

def stat_reset():
    stat_change('HP','20')
    stat_change('GP','0')
    stat_change('Armor','2')
    stat_change('Attack','3')

stat_reset()
inventory_wipe()
ez = open('../www/king.txt','w')
ez.write('HP 40')
ez.close()

new = (tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='door.css'>"))
print(tagger(new,'body',"<p><a href='room1.py'> Enter if you dare </a> <br> <div class='invis'> <a href='equip.py?equip=Key&web=room1.py'> Key for your thoughts? </a> </div> </p>"))
