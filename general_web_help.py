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
print(tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='door.css'>"))
def css(tag, attributes, styles):
# tag, attributes and style should be a list
# lists within lists for attributes and styles
    css = ''
    for ind,ele in enumerate(tag):
        css += ele + ' { \n'
        for sub_ind,sub_ele in enumerate(attributes[ind]):
            css += sub_ele + ': ' + styles[ind][sub_ind] + '; \n'
        css += '     } \n\n'
    return(css)
print(css(['body'], [['background']],[['url("door-pixilart.png") no-repeat fixed center']]))

def stat_get(stat):
    file = open('../www/stats.txt', 'r')
    red = file.read()
    red = red.split('\n')
    red = ' '.join(red)
    red = red.split(' ')
    ind = red.index(stat)
    return(red[ind+1])

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
    
def inventory_add(item):
    r = open('../www/inventory.txt','a')
    r.write(item + '\n')
    r.close()
    
def inventory_wipe():
    r = open('../www/inventory.txt','w')
    r.close()

def inventory_get(item):
    r = open('../www/inventory.txt','r')
    red = r.read()
    red = red.split('\n')
    x = True
    for i in red:
        if i == item:
            x = False
            break        
    if x:
        return('Sadly, you do not have that item.')
    else:
        return('Here is your ' + item + '!')

def stat_reset():
    stat_change('HP','20')
    stat_change('GP','0')
    stat_change('Armor','2')
    stat_change('Attack','3')