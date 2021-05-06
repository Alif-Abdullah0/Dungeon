#!/usr/bin/python
print('Content-type: text/html\n')

import cgi
data = cgi.FieldStorage()

import cgitb
cgitb.enable()

import random

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()
 
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

def inventory_add(item):
    r = open('../www/inventory.txt','a')
    r.write(item + '\n')
    r.close()

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

def stat_get(stat):
    file = open('../www/stats.txt', 'r')
    red = file.read()
    red = red.split('\n')
    red = ' '.join(red)
    red = red.split(' ')
    ind = red.index(stat)
    return(int(red[ind+1]))

def stat_get_s(file,stat):
    file = open(('../www/' + file), 'r')
    red = file.read()
    red = red.split('\n')
    red = ' '.join(red)
    red = red.split(' ')
    ind = red.index(stat)
    return(int(red[ind+1]))

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

def stat_change_s(value):
    file = open('../www/king.txt', 'r')
    red = file.read()
    red = red.split('\n')
    red = ' '.join(red)
    red = red.split(' ')
    ind = red.index('HP')
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
    file = open('../www/king.txt', 'w')
    file.write(red)
    file.close()

Goal = stat_get_s('king.txt','HP')
Armor = stat_get('Armor')

Atk = (random.randrange(5) + stat_get('Attack'))
html = tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='reg.css'>")

Dmg = (random.randrange(4) * random.randrange(5))
Health = stat_get('HP')

Battle = formboi(('bossfight.py?heart=' + str(Goal)),'fight',['o1','o2','o3'],['Attack the king','Try to counter the king','Eat a cookie'])

fight = data.getvalue('fight')
if Goal <= 0:
    print(tagger(html,'body','As you slash your blade into the king, you notice he begins to tremble. As blood splatters from his wound onto your blade, he looks into your eyes, and smiles. Then, he too falls. You gingerly walk over his body, and holding your side to stop the blood loss, ascend the throne. You are the king, now. <a href="final.py"> Sweet Victory </a>'))
elif Health <= 0:
    print(tagger(html,'body','You fall. "Just like everyone else has," the king adds with a smile. "It is over now. Rest up, and try again someday, kid." With that, he looks into your eyes as he plunges his sword into your body. <a href="entry.py"> The end of the beginning </a>'))
else:
    if not('fight' in data):
        fir = tagger(html,'body','The battle has just begin. Both of you are ready for a war. What do you do? <br>')
        print(tagger(fir,'body',Battle))
    else:
        You = tagger(html,'body','You have ' + str(Health) + ' health left! <br>' )
        King = tagger(You,'body','The king has ' + str(Goal) + ' health left! <br>')
        if fight == 'o1':
            Goal -= Atk
            if Atk <= 4:
                hum = 'You hit the king with a glancing blow. Still, it is enough to shake the king up.'
            elif Atk <= 6:
                hum = 'You deliver a solid blow to the king. He winces, then grins right after.'
            else:
                hum = "You nail the king with your strongest shot. He doesn't make a facial expression, but you could tell that it hurt him bad."
            inter = tagger(King,'body',hum)
        elif fight == 'o2':
            if random.randrange(2) == 0:
                Health -= 2 * Dmg
                hum = 'You lose your balance, allowing the king to strike you an extra time.'
            else:
                Goal -= 2 * Atk
                hum = "You perfectly block a shot, and end up hitting the king back."
            inter = tagger(King,'body',hum)
        else:
            if inventory_get("Cookie"):
                stat_change("HP",str(Health + 8))
                hum = "Eating the cookie helped to restore some of your health."
            else:
                hum = "Sadly, you have no more cookies."
            inter = tagger(King,'body',hum)
        stat_change_s(str(Goal))
        stat_change('HP',str((Health) - Dmg))
        
        if Dmg <= 4:
            psg = 'The king hits you firmly with the edge of his sword. The pain feels refreshing.'
        elif Dmg <= 8:
            psg = 'The king strikes your midsection with a sturdy blow from his sword. It is not the worst hit you have taken, but it does hurt a lot.'
        else:
            psg = 'The king delivers a blow so powerful, you feel it through your entire body. You grin and bear it.'
        boss = tagger(inter,'body',('<br> ' + psg))
        print(boss,'body',Battle)
