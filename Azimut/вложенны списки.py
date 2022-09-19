
'''
for i in range(a,b+1):
    print(i,'-',end=' ')
    for j in range(1,i+1):
        if i%j==0:
            print(j,end=' ')
    print()

            
'''

'''
for i in range(0,10):
    for j in range(0,10):
        for l in range(0,10):
            if i!=j and j!=l and i!=l:
                print(i,j,l)
            
'''
for i in range(2,10):
    for j in range(2,10):
        print(i,'*',j,'=',i*j,sep='')
    print('',end='     ')
