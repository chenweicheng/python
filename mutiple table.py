number=["壹","貳","參","肆","伍","陸","柒","捌","玖","拾"]
for x in range(0,9):
	for y in range(0,9):
		
		print(number[x],"*",number[y],"= ",end="")
		sum=(x+1)*(y+1)
		
		if sum > 10 :
			n=sum//10
			print(number[n-1],number[9],sep="",end="")
			sum=sum%10
			
		if sum == 10 :
			print(number[9],end="")

		if sum < 10 and sum > 0:
			print(number[sum-1],end="")

		print()

	print()
