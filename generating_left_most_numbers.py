#+=)
n = 1
def tracing(m):
	st = 'file_' + str(count) + '.txt'
	f = open(st,'w')
	f.write(str(m)+'\n')
	while m % 3 != 0 :
		temp = (m-1)%3
		k = (m-1)/3
		if temp == 0 and k % 2 == 1:
				m = k
				f.write(str(m)+'\n')
			#break
		else:
			m = m<<1
			f.write(str(m)+'\n')
	f.close()
	return m
count = 0
f1 = open('list of end branches.txt','w')
while count <100:
	n = 6*n+2
	next = tracing(n)
	f1.write (str(next) + '\n')
	n = next
	count = count + 1
f1.close()
