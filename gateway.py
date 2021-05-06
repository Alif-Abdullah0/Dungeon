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
    
def formboi(file,select_name,option_value,option_name):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    html += '<select name="' + select_name + '"> \n'
    for x in option_value:
        ind = option_value.index(x)
        html += '<option value="' + x + '">' + option_name[ind] + '</option> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)

es = tagger(s,'body','<div class="bg"> </div>')

html = tagger(es, 'head', "<style> body, html {  height: 100%;  margin: 0;}.bg {  background-image: url('red.png');  height: 100%;  background-position: center;  background-repeat: no-repeat;  background-size: cover;} </style> <link rel='stylesheet' type='text/css' href='reg.css'>")

base = tagger(html,'body','"Wait", the shop owner cries form behind you, "What is your name?" <br>')

text = formtext('gateway.py','text','State your name.')
Comic = tagger(base,'body',text)
name = data.getvalue('text')
form = formboi('gateway.py','choice',['o1','o2'],['Give him the heart', 'Refuse to pay and fight'])
if 'text' in data:
    if name == "Comic":
        print(tagger(html,'body','"Well, uh, right this way!" He hands you a key, and says its for the doorway. "Have fun in there!" His voice cracks as he says those two sentences. <br> <a href="boss.py?name=Comic"> Enter through the doorway </a>'))
    else:
        foo = open('../www/names.txt','a')
        foo.write(name + ' <br>')
        foo.close()
        norm = tagger(html,'body','"Huh. Thought you were someone else. Anyway, you are gonna need a key to open that door. Luckily for you, I have that key! And it is yours for the low price of a golden wendigo heart! Been meaning to melt one of them down ever since..." He trails off.')
        fin = tagger(norm,'body',form)
        print(fin)
elif 'choice' in data:
    if data.getvalue('choice') == 'o1':
        if inventory_get('Wendigo Heart'):
            print(tagger(html,'body','"Well, darn my socks! You do have it. After all these years..." His eyes lose focus for a bit, but then he snaps back into attention. "Anyway, here is your key!" <a href=boss.py?name=wendigo> Head on out </a>'))
        else:
            print(tagger(html,'body','"A liar, eh? This is what we do to liars aorund here." He unsheaths a sword from a scabbard that materialised from thin air. "Prepare yourself!" <br> <a href=fight.py?monster=shopkeeper> Fight for your life </a>'))
    else:
        print(tagger(html,'body','The man stretches his body. "I have been meaning to get into a fight for a while now. I must warn you. You really should not want tp fight a shopkeeper. We have an ace up oursleeves. Always." <br> With that, the man pulls out a crossbow. You can barely move before getting hit in the head with a bolt. You see the man grinning as the world starts to lose focus. "In another time, I would have actually fought you with my sword. Who would have thought?" <br> <a href="entry.py"> You have come so far... </a>'))
else:
    print(Comic)

