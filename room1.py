#!/usr/bin/python

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()

print('Content-type: text/html\n')

import cgi
data = cgi.FieldStorage()

import cgitb
cgitb.enable()

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

def formboi(file,select_name,option_value,option_name):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    html += '<select name="' + select_name + '"> \n'
    for x in option_value:
        ind = option_value.index(x)
        html += '<option value="' + x + '">' + option_name[ind] + '</option> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)
held = (formboi('room1.py', 'tri_fir', ['o1','o2','o3'],['Check out the fireplace', 'Investigate the table','Head to the right']))

def tagger(html, tag, content):
    tag = '</' + tag
    x = html
    lonk = x.find(tag)
    ret = x[:lonk] + content + x[lonk:]
    return(ret)
hiya = tagger(s,'body','<div class="bg"> </div> <div class="invis"><a href="equip.py?equip=Firesword&web=room1.py"> I am invisible! </a> </div>')
new = tagger(hiya,'head','<link rel="stylesheet" type="text/css" href="reg.css">')
if 'tri_fir' in data:
    if data.getvalue('tri_fir') == 'o1':
        inventory_wipe()
        stat_reset()
        nor = (tagger(new,'body',"The fireplace lights up again. Unfortunately, you were standing too close too it. You're journey has come to an end."))
        held = (tagger(nor,'body',"<a href='entry.py'> Return </a>"))
        print(held)
    elif data.getvalue('tri_fir') == 'o2':
        nor = (tagger(new,'body',"As you investigate the table, you notice there is a large crack in the middle of it. You barely touch it, and it breaks, revealing a trap door underneath."))
        print(tagger(nor,'body',"<a href='base.py'>Proceed Below</a>"))
    else:
        nor = (tagger(new,'body',"As you approach the right side of the roomm your mind starts to drift off, until you realize you are back where you started, in the back of the room."))
        print(tagger(nor,'body',"<a href='room1.py'> Time to not waste anymore time. </a>"))
else:
    nor = (tagger(new, 'body', "You are in the first room of the dungeon. In the middle of the room lies a table with a bunch of cards on it. To the left is a fireplace that has been recently extinguished. To the right appears to an open doorway leading to a final boss room... What was to the right again? You're memory clouds over as you ignore the totally unimportant right side of the room."))
    py = (tagger(nor,'body',held))
    print(py)