abcd = ['a', 'b', 'c', 'd']

r=369
end=[]
for i in range(0,r):
	end.append(abcd[i%4])

print(end)	
