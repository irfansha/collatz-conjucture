#+=)
in_file = open("list_primes.txt","r")
out_file = open("tracing_list_primes.txt","w")
data = in_file.readlines()
new_data = []
for num in data:
 temp = int(num)
 new_data.append(temp)
 out_file.write(str(temp)+" ")
 while temp >1:
  if temp%2 == 0:
   temp = temp/2
  else:
   temp = 3*temp  + 1
  if temp in new_data:
   out_file.write(str(temp)+" ") 
   break
  out_file.write(str(temp)+" ")
 out_file.write("\n")
out_file.close()
 
