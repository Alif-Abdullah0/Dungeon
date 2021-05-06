#!/usr/bin/python
print('Content-type: text/html\n')

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()

import cgi
data = cgi.FieldStorage()

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

def formboi(file,select_name,option_value,option_name,file_ret_name=''):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    html += '<select name="' + select_name + '"> \n'
    for x in option_value:
        ind = option_value.index(x)
        html += '<option value="' + x + '">' + option_name[ind] + '</option> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)

def special_formboi(file,select_name,option_value,option_name):
    html = '<form action="'+ file + '" method="GET"' + '>\n' # starting form label
    for y in select_name:
        html += '<select name="' + y + '"> \n'
        list_ind = select_name.index(y)
        for x in option_value[list_ind]: #select options
            ind = option_value[list_ind].index(x)
            html += '<option value="' + x + '">' + option_name[list_ind][ind] + '</option> \n'
        html += '</select> \n'
    html += '<input type="submit"> \n </form>'
    return(html)
form = (special_formboi('catacombs.py',['dir0','dir1','dir2'],[['o1','o2','o3'],['o1','o2','o3'],['o1','o2','o3']],[['Head left','Head right','Go all the way back'],['Head left','Head right','Go all the way back'],['Head left','Head right','Go all the way back']]))
def tagger(html, tag, content):
    tag = '</' + tag
    x = html
    lonk = x.find(tag)
    ret = x[:lonk] + content + x[lonk:]
    return(ret)
html = tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='reg.css'>")

cort = tagger(html,'body',"As you walk through the catacombs, you start feel claustrophobic. The stone walls narrow in very sharply, providing almost no room to move forward with. You see several effigies on the walls. Strangely enough, they all resemble people familiar to you. As you tread forward, you see that the path head forks off. What do you do?")


d0 = data.getvalue('dir0')

d1 = data.getvalue('dir1')

d2 = data.getvalue('dir2')

test = formboi('fountain.py','key',['o1','o2'],['I use my key.', 'I do not have the key.'])

if 'dir0' in data and 'dir1' in data and 'dir2' in data:
    if d0 == 'o3' or d1 == 'o3' or d2 == 'o3':
        fight = (tagger(html,'body','Your fears get the best of you, and you decide to head back the way you came. <br>'))
        print (tagger(fight,'body','<a href="fight.py?monster=wendigo"> Return to the room below the trapdoor. </a>'))
    elif d0 == 'o1' and d1 == 'o2':
        new = tagger(html,'body','You end up at a doorway. You try to open it, but it remains firmly shut. You need a certain key to open the door.')
        print(tagger(new,'body',test))
    else:
        inventory_wipe()
        stat_reset()
        wander = tagger(html,'body','As you wander through the hallways of the catacombs, you realize you are lost. You cannot remember the way you came from, and the path ahead of you keeps going. Your journey has come to an end.')
        print(tagger(wander,'body','<a href="entry.py"> Start over </a>'))
else:
    print(tagger(html,'body',form))