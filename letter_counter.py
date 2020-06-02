import matplotlib.pyplot as plt
f = open("input.txt", "r")
f_out = open("output.txt", "w")
file_content = f.read()

vokal_array = ['a', 'e', 'i', 'o', 'u', 'y']
n = len(vokal_array)
telle_array = [0]*n

for i in file_content:
	index = 0
	for k in vokal_array:
		if (i.lower() == k):
			telle_array[index] = telle_array[index] + 1
		index = index + 1

index = 0
for k in vokal_array:		
	f_out.write(k)
	f_out.write(": ")
	f_out.write(str(telle_array[index]))
	f_out.write("\n")
	index = index + 1
 
f.close()
f_out.close()

plt.bar(vokal_array,telle_array)
plt.show()
print("Successful")
#f = open("input.txt","r") #Åpne fila vi skal telle vokaler i med lesetilgang
#
#f_out = open("output.txt","w") #Åpne utskriftsfil for å lagre data
#
#file_content = f.read() #Lagre innhold i fila til file_content som en string
#
#count = 0
#
#for i in file_content:
#	if (i == 'a') or (i == 'A'):
#		count = count + 1
#		
#print(count)
#
#f_out.write("A or a: ") #Skriv til output.txt om
#f_out.write(str(count)) #hvor mange store og små A'er vi fant
#
#f.close() #Alltid lukk fila etter bruk
#f_out.close()