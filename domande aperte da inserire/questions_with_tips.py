import random
import os

''' How to...

Go to the end end insert the questions like you see in lista_domande

you can put more possible answers using #

you can add a list of possible answer in the question with #

'''

def add_questions(lista_domande):
	''' creates a string with all call to input with questions and answer to be shown '''

	inp = ""
	for d in lista_domande:
		if "#" in d[0]:
			question = d[0].split("#")[0]
			possible = d[0].split("#")[1:]
			possible = "[" + ",".join(possible) + "]"
			inp += f"""input("{question}<br>{possible}", "{d[1]}");\n"""
		else:
			inp += f"""input("{d[0]}", "{d[1]}");\n"""

	return inp


def start(title):

	style = """
	<style> 
		.fontbig {font-size: 1.5em; } 
		body, html {
			background: #ECEDEF;
			margin-left: 10%;
			margin-right: 10%;
			padding: 0; }
	</style>"""

	check = """
		<html oncontextmenu="return false;">
		<script>
		const rightcolor = 'yellow'
		const wrongcolor = "red";
		function check(inp_text, giusta){
			let lista_esatte = giusta.split("#"); // right answers
			let user_input = inp_text.value.toString();       // user input
			if (lista_esatte.includes(user_input.toLowerCase())){
				inp_text.style.background = rightcolor; // turns yellow if right
				return inp_text.value;
			}
			else{
				inp_text.style.background = wrongcolor; // turn red if wrong
		} }"""

	inputs = """ 
		var countdom = 1;

		function input(domanda, giusta){
			var dom_h2 = "<table style='background:#fcab41;'><td><p class='fontbig' style='color: blue'>" + countdom++ + " " + domanda;

			var part1 = dom_h2 + "<br><i style='color:red'>Answer and press return</i><br><input id='casella' class='fontbig' type=text class='t1' placeholder='?...' onchange=\\"if (check(this,'";
			
			part1 += giusta + "'));\\" style='text-align:right'/></center></p></table><br>";
			
			document.write(part1);
			}
		</script>
		
		<h1>TITOLO</h1>
		
				"""
	html = style + check + inputs

	# creates all the input("question", "answer") string
	html += f"<h1>{title}</h1>"
	pa = possible_answers(lista_domande)
	random.shuffle(pa)
	html += "[" + ",".join(pa) + "]"
	html += "<script>" + add_questions(lista_domande) + "</script>"
	save_file(html)


def possible_answers(lista_domande):
	html = []
	for ans in lista_domande:
		html.append(ans[1])
	return html


def save_file(html):
	with open(f"{filename}.html", "w", encoding="utf-8") as file:
		file.write(html)
	os.startfile(f"{filename}.html")




# ===== Customize your quiz ================== >>>

'''
the sign '#' in the question puts a list of possible answers
the sign '#' in the answer puts alternative right answers
'''


filename = "banca"
title = "La banca"
lista_domande = [
# "question", "answer#another right answer#..."
	["Chi sono i principali soggetti in disavanzo?", "imprese"],
	["La banca ha la sua principale attivita' nell'intermediazione ...c", "creditizia"],

]

# ==================== END customization =============== !!!

start(title)