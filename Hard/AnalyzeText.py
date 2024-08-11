def rreplace(string: str, find: str, replace: str, n_occurences: int) -> str:
    temp = string.rsplit(find, n_occurences)
    return replace.join(temp)

contador = 0
print("For this program to work, create a text file and change the path below with the path to your text file.\n")

file = open("C:/Users/User/Desktop/Testes em Python/Hard/Archive.txt", "r")
with file as archive:
    lines = archive.readlines()
    strArc = ''.join(lines)

print(strArc)

strArc = rreplace(string = strArc, find = '.', replace='', n_occurences = strArc.count('.') - 0)
strArc = rreplace(string = strArc, find = '?', replace='', n_occurences = strArc.count('?') - 0)
strArc = rreplace(string = strArc, find = '!', replace='', n_occurences = strArc.count('!') - 0)
strArc = rreplace(string = strArc, find = ',', replace='', n_occurences = strArc.count(',') - 0)

findWord = input("\nWhat word do you want to know how many times shows up? ")
for word in strArc.split():
	if word.lower() == findWord.lower():
		contador += 1

print("Your word appear", contador, "times!")

file.close()