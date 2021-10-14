# A script to make tests in javascript with python
import os
import re

# List of lists with datas for the questions; each has 1.image 2.question 3.answer all as strings
# Adds the initial script and the html code with the questions
style = """<style> body {font-size : 2em; } input {font-size: 3em;width:100%; background: cyan; } button { font-size: 3em; } </style> """


# Here goes the function that checks if the answer is right
function = """<script>
function code(val, sol){ if (val==sol) return 1;}
</script>
"""
# This is the input text template that will be used to create the questions

but = """<button id="---idbut---1" value="1" onclick="x=code(this.value, '--soluzione--');console.log(this.value);if (x==1){this.style.background='yellow';--xxx--.value='ok'}; if (x!=1){ --xxx--.value='no'};---idbut---1.disabled=true;---idbut---2.disabled=true;---idbut---3.disabled=true;--xxx--.disabled=true">1</button>---ans1---<br>"""
but += """<button id="---idbut---2" value="2" onclick="x=code(this.value, '--soluzione--');console.log(this.value);if (x==2){this.style.background='yellow';--xxx--.value='ok'}; if (x!=2){ --xxx--.value='no';---idbut---1.disabled=true;---idbut---2.disabled=true;---idbut---3.disabled=true;--xxx--.disabled=true}"">2</button>---ans2---<br>"""
but += """<button id="---idbut---3" value="3" onclick="x=code(this.value, '--soluzione--');console.log(this.value);if (x==3){this.style.background='yellow';--xxx--.value='ok'}; if (x!=3){ --xxx--.value='no';---idbut---1.disabled=true;---idbut---2.disabled=true;---idbut---3.disabled=true;--xxx--.disabled=true}"">3</button>---ans3---<br>"""

tpl = """<br>--img--<b>--question--</b>
---but---"""

text = """
<input id="--xxx--" type="text" onchange="x=code(this.value, '--soluzione--');if (x==1){this.style.background='yellow'};--xxx--.disabled=true">
"""

def add_tag_to(text):
    # * is for header 2
    #search all the words with a *
    # You need a \*, because * has a meaning in regex
    pattern = "\*.+"
    h1 = re.findall(pattern, text)
    for word in h1:
        word = word.replace("*", "")
        tagged = re.sub(pattern, f"<h2>{word}</h2>", text)
        # delete that \n from <h2> line, to avoid double <br>
        tagged = tagged.replace("\n", "")
    # ============================ header 2
    # This will add a break to every \n, to avoid having to add it manually
    tagged = re.sub("\n", "<br>", tagged)
    return tagged

def create_html(traccia1, sol):
    "This returns the html code with the questions and input boxes"
    imgurl = "http://icons.iconarchive.com/icons/tatice/cristal-intense/256/Question-icon.png"

    # This adds some shortcut to html tags in the text (see the function)
    traccia1 = add_tag_to(traccia1)
    imgtag = "<img src='" + imgurl + "'' width=50/>"
    html = style + traccia1 + function
    counter = 0
    # substitute the placeholders with data
    for qns in sol:
        template = tpl
        if len(qns) == 1:
            template = qns[0]
        else:
            # if you add a paragraph as second item it package it as a regular 2 item list
            if "-but-" in qns[0]:
                template = template.replace("---but---", but)
                qns[0] = qns[0].replace("-but-", "...")
                template = template.replace("---idbut---", "idbut" + str(counter))
                #qns[1] = "<ol>" + "<li>".join(qns[1].split("#")) + "</ol>"

            else:
                template = template.replace("---but---", "")
                template = template + text

            template = template.replace("--img--", imgtag)
            template = template.replace("--question--", qns[0])
            #
            if "..." not in qns[0]:
                template = template.replace("--soluzione--", qns[1])
            else:
                template = template.replace("...", "")
            template = template.replace("--xxx--", "id" + str(counter))
            template += "<hr>"
            counter += 1
        html += template
    return html

def save(html):
    # Saves the html file with the code created above
    with open("esempio.html", "w") as file:
        file.write(html)
    # shows the file in the browser
    os.startfile("esempio.html")