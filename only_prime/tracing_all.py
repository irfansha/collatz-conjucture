#+=)
out_file = open("tracing_list.txt","w")
new_data = []
for num in range(1,100):
 temp = num
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
 
