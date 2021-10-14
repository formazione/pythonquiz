import random
import sys

print(sys.version)
tmp = "Calcola l'interesse su 10.000 € al tasso del 7% per 1 anno."

def genex():
	s = {
		s["Capitale"] : random.randrange(100, 1000, 100),
		s["tasso"] : random.randint(2,9),
		s["final"] : ""
	}
	C = s["Capitale"] = random.randrange(100, 1000, 100)
	r = s["tasso"] = random.randint(2,9)
	s["year_m_d"] = random.choice(["anni", "mesi", "giorni"])

	# =========== change the formula depending on time ========
	if s["year_m_d"] == "anni":
		t = s["tempo"] = random.randint(1, 5)
		s["interessi"] = C*r*t/100
	if s["year_m_d"] == "mesi":
		t = s["tempo"] = random.randint(1, 11)
		s["interessi"] = C*r*t/1200
	if s["year_m_d"] == "giorni":
		t = s["tempo"] = random.randint(1, 250)
		s["interessi"] = C*r*t/36500

	# ================ Change final for 1 or more years, months, days
	if t > 1:
		s["final"] = "i"
	else:
		if s["year_m_d"] == "mesi":
			s["final"] = "e"
		else:
			s["final"] = "o"

	# === Change solution to int and adding a 0
	if s["interessi"] == int(s["interessi"]):
		s["interessi"] = int(s["interessi"])
	else:
		s["interessi"] = str(round(s["interessi"], 2))
		if len(s["interessi"].split(".")[1]) == 1:
			s["interessi"] = s["interessi"] + " " + s["interessi"] + "0"
		add = s["interessi"].replace(".", ",")
		s["interessi"] = s["interessi"] + " " + add

	return s

def printex():
	s = genex()
	s["year_m_d"] = s["year_m_d"][:-1]
	print("input(\"Calcola l'interesse su {Capitale} € al tasso del {tasso} % per {tempo} {year_m_d}{final}\", \"{interessi}\");".format(**s))


def dom(domanda, risposta):
	print(f"input(\"{domanda}\",{risposta});")

def show():
	print("""
<style>
body{
	margin: 10%;
}
	.fontbig {
		font-size: 1.5em;
	}
</style>
<body oncontextmenu="return false;">
<script>

function check(casella, giusta, num){
	// the solutions are good both for low and capital letters
	if (giusta.includes(casella.value.toLowerCase())){
		casella.style.background = 'yellow';
		return casella.value.includes(giusta);
	}
	else{
		casella.style.background = 'red';
	}
}

function print_it(parola){
	if (soluzioni.innerHTML.includes(parola)){
	}
	else {
    	soluzioni.innerHTML += " - " + parola;
	}
}

var countdom = 1;
function input(domanda, giusta){
	var dom_h2 = "<table style='background:#fcab41;'><td><p class='fontbig' style='color: blue'>" + countdom++ + " " + domanda;
	var part1 = dom_h2 + "<center><input id='casella' class='fontbig' type=text class='t1' placeholder='?...' onchange=\\"if (check(this,'";
	part1 += giusta + "')){print_it(this.value)};\\" /></center></p></table><br>";
	document.write(part1);
	}
	

x = document.getElementsByClassName('t1');
for (i of x){
    i.value = "";
}

</script><script>
		""")
	
	dom("Quando è nata l'OMT?", ["1975", "nel 1975"])
	
	dom("Come si calcola la permanenza media? Presenze / ....",
		["arrivi"]);

	
	print("</script>")
show()