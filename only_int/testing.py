import numpy as np
import matplotlib.pyplot as plt
data = []
in_file = open("39_iter.txt","r")
lines = in_file.readlines()
for line in lines:
 words = line.split(" ")
 a = words[0]
 b = words[1]
 c = int(a)/int(b)
 data.append(c)
data = list(set(data))
data.sort()
x = data
y =range(len(data))
print x
#print y

plt.plot(x,y,'o')

plt.show()

