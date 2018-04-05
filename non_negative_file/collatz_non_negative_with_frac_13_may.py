#+=)
for num in range(2,20):
 in_name = str(num-1) + "_iter.txt"
 out_name = str(num) + "_iter.txt"
 in_file = open(in_name,"r")
 out_file = open(out_name,"w")
 lines = in_file.readlines()
 for line in lines:
  words = line.split(" ")
  a = int(words[0])
  b = int(words[1])
  if ((2*a)/b)>0:
   out_file.write(str(2*a) + " " + str(b) + " " + "\n")
  if ((a-b)/(3*b))>0:  
   out_file.write(str(a-b) + " " +str(3*b) + " " + "\n" )
 in_file.close()
 out_file.close()
