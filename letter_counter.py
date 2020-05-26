f = open("input.txt", "r")
f_out = open("output.txt", "w")

file_content = f.read()

count_a = 0

for i in file_content:
	if (i == 'a') or (i == 'A'):
		count_a = count_a + 1;
	
f_out.write("A or a: ")
f_out.write(str(count_a))
f_out.write("\n")
 
f.close()
f_out.close()
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