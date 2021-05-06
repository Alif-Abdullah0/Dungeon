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
    
def formboi(file,select_name,option_value,option_name):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    html += '<select name="' + select_name + '"> \n'
    for x in option_value:
        ind = option_value.index(x)
        html += '<option value="' + x + '">' + option_name[ind] + '</option> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)

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

end = data.getvalue('name')

html = tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='reg.css'>")
new = tagger(html,'body','You see a man sitting in a golden throne. He wears a wooden crown. The wall behind him has been split into two pieces. ')
if end == 'Comic':
    stat_change('HP','25')
    nor = tagger(new,'body','"Comic, huh?" You stand there, confused that the king knows your name. "So the legends are true. Huh." He throws his head back and laughs, before locking eyes with you. "LET US SEE YOUR STRENGTH." He waves his hand around, and you feel your wounds disappear. "It would not be fun if the battle was not fair, no?" <br> <a href="bossfight.py?health=40"> Cue the boss music! </a>')
    print(nor)
elif end == 'wendigo':
    print(tagger(new,'body','"How could you?" You stand there, confused. "How could you kill my brother," the king asks. You think the king reminds you of someone, and then you realize that he bears an uncanny resemblance to the wendigo you had slain. "There will be no mercy for you." As soon as he sees that, you feel a dampness inside of your armor. You look down, and to your horror, blood is falling from your breastplate. You drop, dead, to the ground. <br> <a href="entry.py"> Begin again </a>'))
else:
    print(tagger(new,'body','"Is it odd to say that I have been expecting you? You, a blight on my peaceful abode. You, who killed my friends, then ravaged my home and murdered it subjects. I have lost the will to fight. I surrender the throne, KING. May you prosper in your affairs." As you try to get a word in, you notice that the king has pulled out a dagger from his robes. You stand there, shocked, as he raises it to the heavens. A second later,lightning ignites the king on fire, and a cloud of smoke envelops the king, and he is gone. You do not know what to make of the situation, but decide to ascend the throne. You are the king now, after all. <br> <a href="final.py"> Induction ceremony </a>'))

