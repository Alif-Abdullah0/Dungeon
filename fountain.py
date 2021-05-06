#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()

import cgi
data = cgi.FieldStorage()

import random

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()

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
    
def inventory_wipe():
    r = open('../www/inventory.txt','w')
    r.close()

def formboi(file,select_name,option_value,option_name):
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

html = tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='reg.css'>")

key = data.getvalue('key')

def inventory_get(item):
    r = open('../www/inventory.txt','r')
    red = r.read()
    red = red.split('\n')
    x =  False
    for i in red:
        if i == item:
            x = True
            break
    if x:
        return(True)
    else:
        return(False)

def inventory_wipe():
    r = open('../www/inventory.txt','w')
    r.close()

def stat_reset():
    stat_change('HP','20')
    stat_change('GP','0')
    stat_change('Armor','2')
    stat_change('Attack','3')

if key == 'o1':
    if inventory_get('Key'):
        cort = tagger(html,'body','<h1> The door has opened! </h1> <br> Behind the door is an entirely white room, empty except for the fountain in the middle. You are too thirsty to do anything besides take a drink. Upon doing so, you find that the water is... <br>')
        if random.randrange(2) == 0:
            inventory_wipe()
            stat_reset()
            fin = tagger(cort,'body','Poisonous! You drop dead in the fountain room. The door closes behind you. <a href="entry.p"> Try again </a>')
            print(fin)
        else:
            stat_change('HP','30')
            fin = tagger(cort,'body','Refreshing! After drinking your fill of the water, you notice that the door behind you has closed. You attempt to open it, but find that neither brute strength or your key can allow you to open. However, a replica door has appeared on the other side of the fountain. Your only option is to try and open it, and to your surprise, the door does open. <br> <a href="shop.py?enter=fountain"> Walk through </a>')
        print(fin)
    else:
        fin = tagger(html,'body','The door opens its eye. LIARS WILL BE TERMINATED. That is the last thing you here before you are vaporized. <br> <a href="entry.py>"> Getting vaporized sure does suck, huh? </a>')
        print(fin)
else:
    if inventory_get('Key'):
        fin = tagger(html,'body','The door opens its mouth. "That key is too dangerous to be left with a scoundrel like you." You respond by hitting it with your sword. <br> <a href=fight.py?monster=door> Commence the battle! </a>')
        print(fin)
    else:
        inventory_wipe()
        stat_reset()
        fin = tagger(html,'body','You decide to head back to the main room. As you start to leave, your vision gets kind of blurry. You soon pass out. Waking up, you find you are at the front door of the dungeon. Al<a href="entry.py"> ')
        print(fin)
        
    
    