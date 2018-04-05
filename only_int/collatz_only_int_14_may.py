#+=)
for num in range(20,40):
 in_name = str(num-1) + "_iter.txt"
 out_name = str(num) + "_iter.txt"
 in_file = open(in_name,"r")
 out_file = open(out_name,"w")
 lines = in_file.readlines()
 for line in lines:
  words = line.split(" ")
  a = int(words[0])
  b = int(words[1])
  x = (float(2*a)/float(b))
  y = (float(a-b)/float(3*b))
  if x >0 and x.is_integer():
   out_file.write(str(2*a) + " " + str(b) + " " + "\n")
  if y>0 and y.is_integer():  
   out_file.write(str(a-b) + " " +str(3*b) + " " + "\n" )
 in_file.close()
 out_file.close()
