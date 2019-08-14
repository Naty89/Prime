def stop(x):	
	while [ i for i in range(2,x) if x%i==0 ]:
		x +=1
	return x	


print(stop(7))
print(stop(22))
print(stop(44))