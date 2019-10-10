print('这是一个99乘法表')
for i in range(1,10):
    for j in range(1,10):
	    if i>=j:
		    print('%sx%s=%s'%(j,i,i*j),end=' ')
    print()
