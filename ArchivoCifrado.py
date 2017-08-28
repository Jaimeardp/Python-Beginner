print "Ingres una opcion"
print "1.Esrcibir en el archivo con cifrado\n2.Leer el archivo cifrado"

op = raw_input("Ingrese la opcion")

if int(op) == 1:
	archi = open('texto.txt','a')
	msm = raw_input("Ingrese el parrafo : ")

	lisNom = list()
	listCod = list()
	lista = list()

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

	cifrarMen(msm)		
	delimitador = ' '
	cad =  delimitador.join(listCod)
	#print cad
	archi.write("\n")
	archi.write(cad)

if int(op) == 2:
	archi = open('texto.txt','r')

	def descifra(li):
			cad = "" 
			for n in li:
				aum = 0
				aux = 1
				while aux < len(n):
					i = n[aum:aux+1]
					num = int(i)
					#print num
					#print aum," : ",aux
					if num in range(32,165):
						cad += chr(num)
						aum = aux + 1
						aux = aum 

					aux = aux+1
				cad+= " "
			print cad

	for linea in archi:
		linea = linea.rstrip()
		palabras = linea.split()
		descifra(palabras)

				

