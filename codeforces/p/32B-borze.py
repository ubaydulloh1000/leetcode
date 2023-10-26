borze = input()

alphabet = {
	".": "0",
	"-.": "1",
	"--": "2"
}

decode = ""
while borze:
	if len(borze) < 2:
		decode += alphabet[borze[0]]
		borze = ""
	elif borze[:2] == "--":
		decode += alphabet["--"]
		borze = borze[2:]
	elif borze[:2] == "-.":
		decode += alphabet["-."]
		borze = borze[2:]
	elif borze[0] == ".":
		decode += alphabet["."]
		borze = borze[1:]


print(decode)
