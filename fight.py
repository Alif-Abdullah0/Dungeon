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

Health = stat_get('HP')
Armor = stat_get('Armor')
Attack = stat_get('Attack')

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
    
crea = data.getvalue('monster')

html = tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='reg.css'>")

dialouge = tagger(html,'body','<h1> You encounter a hostile' + crea + '</h1> <br> It attacks you. The battle begins! <br> *Most battles in the dungeon are decided via our battle algorithm.* <br>')

def battle(hum_a,hum_d,hum_h,mon_h,mon_a):
    html = ''
    hum_a = int(hum_a)
    hum_d = int(hum_d)
    if int(hum_h) <= 0:
        html += ('You have fallen in combat. <br> <a href="entry.py"> Click here to try the dungeon once more. </a>')
        stat_change('HP','20')
        stat_change('GP','0')
        stat_change('Armor','2')
        stat_change('Attack','3')
        return(html)
    elif int(mon_h) <= 0:
        html += 'You have beaten the creature, with '+ str(hum_h) +' health left. '
        if crea == 'wendigo':
            inventory_add("Wendigo Heart")
            html += 'You have gained three pieces of gold! You see something gold in the center of the chest of the wendigo. After putting it into your inventory sack, you realize that it is its heart. However, you cannot pull it off the inside of your burlap sack. <br> At this point, you start to feel a bit woozy from all the blood loss, however. <br> <a href="shop.py"> You begin to pass out </a>'
        elif crea == 'spider':
            html += 'You have gained two pieces of gold! <br> Cleaning the spider guts off of your blade, you move on. <br> <a href="shop.py"> Leave the cathedral </a>'
        elif crea == 'door':
            html += 'After hacking down the door, you feel a sudden shift in the weight of your burlap sack. You realize that defeating the door has given you a 100 gold piece! You do hear some footsteps in the catacomb paths around you. Time to leave, before anyone finds you here. <br> <a href="cathedral.py"> Head for the cathedral! </a>'
        else:
            html += '<br> As you watch the light fade from the eyes of the stand owner, you notice a key fall out of his pocket. It fits perfectly into the keyhole of the door across the room. Turning the key, you are greeted by a bright stream of light. <br> <a href=boss.py> Head in </a>'
        stat_change('HP',str(hum_h))
        return(html)
    else:
        hum_h = (int(hum_d) + int(hum_h)) - (mon_a + random.randrange(1,((mon_a*2) - 1)))
        mon_h = (mon_h - (random.randrange(5) + int(hum_a)))
        return(battle(hum_a,hum_d,hum_h,mon_h,mon_a))

def fight(HP,DEF,ATK):
    if 'monster' in data:        
        if crea == 'wendigo':
            extra = (battle(ATK,DEF,HP,25,3))
            stat_change('GP',str(stat_get('GP') + 3))
            return(tagger(dialouge,'body',extra))
        elif crea == 'spider':
            extra = battle(ATK,DEF,HP,12,2)
            stat_change('GP',str(stat_get('GP') + 2))
            return(tagger(dialouge,'body',extra))
        elif crea == 'door':
            extra = battle(ATK,DEF,HP,50,2)
            stat_change('GP',str(stat_get('GP') + 100))
            return(tagger(dialouge,'body',extra))
        else:
            extra = battle(ATK,DEF,HP,30,3) 
            return(tagger(dialouge,'body',extra))
    else:
        return(tagger(dialouge,'body',"Well this is awkward. You're not supposed to be back here!"))
print(fight(Health,Armor,Attack))

