#+=)
import math
n = 21
k = 1365
out_file = open("test_dot"+str(k)+".txt","w")
out_file.write("digraph"+" "+"graphname{"+"\n")    #graph graphname {
for num in range(0,n):
  p_num = k*int(math.pow(2,num))
  if (p_num - 1)%3 == 0:
   out_file.write(str((p_num - 1)/3)+"->"+str(p_num)+";"+"\n")
   out_file.write(str(2*p_num)+"->"+str(p_num)+";"+"\n")
  else:
    out_file.write(str(2*p_num)+"->"+str(p_num)+";"+"\n")
out_file.write("}")
out_file.close()
 
