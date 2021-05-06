#!/usr/bin/python
print('Content-type: text/html\n')

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()

import cgi
data = cgi.FieldStorage()

import cgitb
cgitb.enable()

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
get = data.getvalue('choi')
spooder = data.getvalue('dec')

form = formboi('cathedral.py','choi',['01','02'],['Check out the cobweb','Leave through the doorway on the opposite side of the room.'])
spider_choice = formboi('cathedral.py','dec',['o1','o2'],['Fight the spider!','Can we not fight?'])
es = tagger(s,'body','<div class="bg"> </div>')
html = tagger(es, 'head', "<style> body, html {  height: 100%;  margin: 0;}.bg {  background-image: url('cathedral.png');  height: 100%;  background-position: center;  background-repeat: no-repeat;  background-size: cover;} </style> <link rel='stylesheet' type='text/css' href='reg.css'>")

if spooder == 'o1':
    spood = tagger(html,'body','Commence the battle! <br>')
    print(tagger(spood,'body','<a href="fight.py?monster=spider"> Fight! </a>'))
elif spooder == 'o2':
    spood = tagger(html,'body','"I guess so." The spider turns around around and starts fidgeting with its web. <br> <a href="shop.py"> Leave the cathedral. There is nothing else of interest. </a>')
    print(spood)
elif get == '01':
    search = tagger(html,'body','You decide to inspect one of the cobwebs. A spider jumps out at you!')
    print(tagger(search,'body',spider_choice))
elif get == '02':
    print(tagger(html,'body','You decide to simply leave the room. <br> <a href="shop.py"> Open the door. </a>'))
else:
    inter0 = tagger(html,'body','You walk into the cathedral. It seems to have been abandoned. There are cobwebs strewn about in the corner, and there is a red door at the other end of the hallway. It is calling to you. What do you do?')
    inter1 = tagger(inter0,'body',form)
    print(inter1)

