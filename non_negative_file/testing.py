import numpy as np
import matplotlib.pyplot as plt
data = []
data1 = []
in_file = open("19_iter.txt","r")
lines = in_file.readlines()
for line in lines:
 words = line.split(" ")
 a = words[0]
 b = words[1]
 c = float(a)/float(b)
 data.append(c)
 if c.is_integer() and c > 0:
  data1.append(int(c))
data.sort()
x = data
y =range(len(data))
print x
#print y

plt.plot(x,y,'o')

data = list(set(data))
data.sort()
x = data
y =range(len(data))
print x
#print y

plt.plot(x,y,'o')

data1 = list(set(data1))
data1.sort()
x = data1
y =range(len(data1))
print x
#print y

plt.plot(x,y,'o')

plt.show()

