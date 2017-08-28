import numpy as np 
sum = 0

dig = raw_input('choose ')
aux1 = ' '.join(str(dig))
lbb = aux1.split(' ')
aux = 0
lis = []
#------------------
num = raw_input('matriz ')
aux = ' '.join(str(num))
lx = aux.split(' ')
arr = np.array(lx)
arr.shape = (3,3)
# -------------
for i in lbb:
	tp = np.where(arr==i)
	print(tp)

	if aux == i:
		lis.append((tp[0]+1,tp[1]))
		lis.append((tp[0],tp[1]+1))
		lis.append((tp[0]+1,tp[1]+1))

		lis.append((tp[0]-1,tp[1]))
		lis.append((tp[0],tp[1]-1))
		lis.append((tp[0]-1,tp[1]-1))

		lis.append((tp[0]+1,tp[1]-1))
		lis.append((tp[0]-1,tp[1]+1))
		continue

	aux = i

	if(tp == (1,1)):
		sum = sum +1
		lis = []
		lis.append((tp[0]+1,tp[1]))
		lis.append((tp[0],tp[1]+1))
		lis.append((tp[0]+1,tp[1]+1))

		lis.append((tp[0]-1,tp[1]))
		lis.append((tp[0],tp[1]-1))
		lis.append((tp[0]-1,tp[1]-1))

		lis.append((tp[0]+1,tp[1]-1))
		lis.append((tp[0]-1,tp[1]+1))
		continue

	if tp in lis:
		sum = sum + 1
		#print lis
		print 'aca'
		lis = []
	else:
		sum = sum + 2
		#print lis
		print 'asas'
		lis = []

	lis.append((tp[0]+1,tp[1]))
	lis.append((tp[0],tp[1]+1))
	lis.append((tp[0]+1,tp[1]+1))

	lis.append((tp[0]-1,tp[1]))
	lis.append((tp[0],tp[1]-1))
	lis.append((tp[0]-1,tp[1]-1))

	lis.append((tp[0]+1,tp[1]-1))
	lis.append((tp[0]-1,tp[1]+1))

	#		
if lbb[0] == arr[1,1]:
	sum = sum -1
else:
	sum = sum -2

#sum = sum - 2

print sum








