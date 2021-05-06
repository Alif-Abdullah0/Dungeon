#!/usr/bin/python
print('Content-type: text/html\n')

f = open('html.txt')
s = f.read()
s = s.strip()
f.close()

import cgi
data = cgi.FieldStorage()

def formboi(file,select_name,option_value,option_name,file_ret_name=''):
    html = '<form action="'+ file + '" method="GET"' + '>\n'
    html += '<select name="' + select_name + '"> \n'
    for x in option_value:
        ind = option_value.index(x)
        html += '<option value="' + x + '">' + option_name[ind] + '</option> \n'
    html += '</select> \n <input type="submit"> \n </form>'
    return(html)
form = (formboi('base.py', 'base', ['o1','o2','o3','o4'],['Check out the bone stash', 'Take the catacombs door', 'Take the cathedral door', 'Thank the sign']))
def tagger(html, tag, content):
    tag = '</' + tag
    x = html
    lonk = x.find(tag)
    ret = x[:lonk] + content + x[lonk:]
    return(ret)
html = tagger(s, 'head', "<link rel='stylesheet' type='text/css' href='reg.css'>")
if 'base' in data:
    if data.getvalue('base') == 'o1':
        inter = tagger(html,'body',"As you run you hands through the bones, you notice that there is a helmet (some would call it a skull). <br> Dare to equip it?")
        link = tagger(inter,'body','<a href="equip.py?equip=Skulmet&web=base.py"> Equip the item? </a> \n')
        fin = tagger(link,'body','<a href="base.py"> Turn Around </a>')
        print(fin)
    elif data.getvalue('base') == 'o2':
        inter = tagger(html,'body','You take the catacombs door. Not much else to say.')
        fin = tagger(inter,'body','<a href="catacombs.py"> Walk under Paris ... I mean through the catacombs </a>')
        print(fin)
    elif data.getvalue('base') == 'o3':
        inter = tagger(html,'body','You walk through the cathedral doorway. yas ot esle hcum toN.')
        fin = tagger(inter,'body','<a href="cathedral.py"> Enter the chamber </a>')
        print(fin)
    else:
        inter = tagger(html,'body',"As you thank the sign, you swear you hear it say 'You're welcome'. All of a sudden, you're mind starts to wander off. Somehow, you're back where you started.")
        print(tagger(inter,'body','<a href="entry.py"> Back to the drawing board. </a>'))
else:
    inter = tagger(html,'body','You take a leap of faith and jump in. The drop down is pretty long. After about five seconds of falling, you start to scream. Thankfully, you hit the ground soon after raising your voice to shout.  Surprisingly, nothing is broken. The room you have fallen into is dimly illuminated with one torch.  You see a stash of bones in one corner of the room (Yes, I mean a stash and not a pile). Turning around, you see two doorways on  the wall opposite of the bone stash. They lead to a cathedral and a courtyard. You know this because a helpful sign above it says so.')
    fin = tagger(inter,'body',form)
    print(fin)
