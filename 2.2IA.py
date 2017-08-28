msm = raw_input("Ingrese mensaje a incriptar : ")

archi=open('texto.txt','w')
archi.close()

archi = open('texto.txt','a')

archi.write(msm)

#---------------------------

dic = dict()
lisNom = list()
listCod = list()
lista = list()

#---------------------------

def sumDigito(num):
	sum = 0 
	cad = str(num)
	for i in cad:
		sum = sum + int(i)
	return sum

def cifrarPal(cad):
	xx=""
	for letra in cad:
		xx += str(ord(letra)) 		
		lista.append(sumDigito( ord(letra))) # <----------- Estetica
	listCod.append(xx)


def cifrarMen(cad):
	l = cad.split()
	for pal in l:
		lisNom.append(pal)
		cifrarPal(pal)
	#print l

def descifra():
	cad = "" 
	for n in listCod:
		aum = 0
		aux = 1
		while aux < len(n):
			i = n[aum:aux+1]
			num = int(i)
			#print num
			#print aum," : ",aux
			if num in range(32,127):
				cad += chr(num)
				aum = aux + 1
				aux = aum 

			aux = aux+1
		cad+= " "
	print cad
				
	

cifrarMen(msm)
i=0
# Llena dicionario con clave y valor : nombre y cifrado en este caso
for x  in lisNom:
	dic[x] = listCod[i]
	i = i +1;

#print dic
#print lista
#print listCod

for nume in lista:
	print nume," ",

print "\n"

descifra()

print "\n"

for nume in listCod:
	print nume," ",