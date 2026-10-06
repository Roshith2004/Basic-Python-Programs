"""

for i in range(5,0,-1):
    print("* "*i)


for i in range(7):
    if i%2==0:
        print(" *"*i)
    else:
        print(" *"*i*2)


n=int(input("enter a number:"))
for i in range(1,11):
    m=n*i
    print(n,"*",i,"=",m)



n=int(input("enter strt number:"))
m=int(input("enter end number:"))
for i in range(n,m+1):
    if i>0:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
    if(c==2):
        print("* "*(i+1))
    else:
        print("* "*i)


for i in range(1,6):
    print(" "*(5-i)+"* "*i)


for i in range(5,0,-1):
    print(" "*(5-i)+"* "*i)

"""
for i in range(1,6):
    print(" "*(5-i)+"* "*i)
    if i==5:
        for i in range(4,0,-1):
            print(" "*(5-i)+"* "*i)