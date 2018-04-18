n=int(input('Nhap n: '))
def inn(n):
	for i in range(1,n+1):
		print(i)
def inchan(n):
	s=0
	for i in range(1,n+1):
		if(i%2==0):
			s+=i
	print('Tong chan: ',s)
inn(n)
inchan(n)
