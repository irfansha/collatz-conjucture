import math
data = []
data.append(2)
for num in range(3,10000000):
 count = 0
 root = math.sqrt(num)
 for check in data:
  if check > root:
	break
  if num %check == 0:
   count = 1
   break
 if count == 0:
  data.append(num)
#print data
 
out_file = open("list_primes.txt","w")
for num in data:
 out_file.write(str(num)+ " "+ "\n")
out_file.close()
