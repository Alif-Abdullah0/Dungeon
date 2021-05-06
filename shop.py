#!/usr/bin/python
print('Content-type: text/html\n')

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

def stat_change(stat,value):
    file = open('../www/stats.txt', 'r')
    red = file.read()
    red = red.split('\n')
    red = ' '.join(red)
    red = red.split(' ')
    ind = red.index(stat)
    red.remove(red[ind+1])
    red.insert(ind+1,str(value))
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

def stat_get(stat):
    file = open('../www/stats.txt', 'r')
    red = file.read()
    red = red.split('\n')
    red = ' '.join(red)
    red = red.split(' ')
    ind = red.index(stat)
    return(int(red[ind+1]))

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

def formboi(file,select_name,option_value,option_name):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    html += '<select name="' + select_name + '"> \n'
    for x in option_value:
        ind = option_value.index(x)
        html += '<option value="' + x + '">' + option_name[ind] + '</option> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)
buy = (formboi('shop.py', 'items', ['o1','o2','o3','o4','o5'],['Buy a Cookie','Get a surgery to increase your maximum health points','Buy a lightsaber','"What are you doing in a dungeon?"','Leave the shop']))

goods = data.getvalue('items')


es = tagger(s,'body','<div class="bg"> </div>')
html = tagger(es, 'head', "<style> body, html {  height: 100%;  margin: 0;}.bg {  background-image: url('shop.png');  height: 100%;  background-position: center;  background-repeat: no-repeat;  background-size: cover;} </style> <link rel='stylesheet' type='text/css' href='reg.css'>")
if (stat_get('GP') <= 0):
    if inventory_get('Cookie'):
        print(tagger(html,'body','"Sorry. Looks like you do not have enough money to buy anything else from me. You do not smell of gold any longer. Good day!" <br> <a href="gateway.py"> Time to go </a>'))
    else:
        print(tagger(html,'body','"Looks like you do not have enough money to buy anything from me. Sucks to hear pal. Oh well." <br> <a href="gateway.py"> Time to go </a>'))
else:
    if goods == 'o1':
        if inventory_get('Cookie'):
            inter = tagger(html,'body','Back for more? I knew you could not resist these. Here!')
        else:
            inter = tagger(html,'body','"Ah yes. These cookies are all that an adventurer needs to outlast a dungeon! There yours, for just a single gold piece." <br>')
        inventory_add('Cookie')
        print(tagger(inter,'body',buy))
    elif goods == 'o2':
        stat_change('GP',(stat_get('GP') - 20))
        stat_change('HP',25)
        if stat_get('HP') == 25:
            inter = tagger(html,'body','"You already got the surgery! If you want to throw away your money though, I am not complaining. What else would you like to buy?"')
        else:
            inter = tagger(html,'body','"You will be worked on by our world class surgeons. They value their privacy, so these measures are necessary." With that, he stabs you with a tranquilizer dart. You did not even see him pull it out. The last thing you hear is, " By the way, that will cost you 25 gold pieces. Of course, if you do not have that, I will take the rest of your gold."')
        print(tagger(inter,'body',buy))
    elif goods == 'o3':
        inter = tagger(html,'body','"An elegant weapon, of a more civilized age. Sadly, your father did not leave you one. No lightsabers for sale!"')
        print(tagger(inter,'body',buy))
    elif goods == 'o4':
        inter = tagger(html,'body','"The market for these goods here is astounding! You would not believe the amount of adventurers, just like you, that I get here. Now, what would you like to buy?"')
        print(tagger(inter,'body',buy))
    elif goods == 'o5':
        if inventory_get('Cookie'):
            print(tagger(html,'body','"Well, have a good day! Try not to die, kiddo." <br> <a href=boss.py> Try not to die indeed </a>'))
        else:
            print(tagger(html,'body','"It is your right to leave without purchasing." As you start to leave, you hear a blade being unsheathed. "Just as it is mine to not respect it!" The merchant bares his teeth, and just by looking at his ferocious maw can you see that he is, in fact, not a human. <br> <a href=fight.py?monster=Comic> Commence the fight! </a> '))
    else:
        intro = tagger(html,'body','<h1> You gaze upon a human merchant at a wooden stand, outside of a large hotel. </h1> "Items for sale!" he yells, over and over. His gaze stops on you. "Hello there! What would you like to buy?" ' )
        fin = tagger(intro,'body',buy)
        print(fin)

