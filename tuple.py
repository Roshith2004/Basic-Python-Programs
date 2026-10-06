#1
"""
x=(11,99,33,22,66)
print("First element:",x[0])
print("Last element:",x[4])

"""
#2
"""
x=("mai","bai","sai","kai","lee")
print("3rd student:",x[2])

"""
#3
"""
x=(2,7,5,8,9)
print(x)
print("No. of elements:",len(x))

"""
#4
"""
x=(3,4,5,3,7,3,3,3)
print(x)
n=int(input("Enter a number:"))
print("Frequency of",n,"is",x.count(n))

"""
#5
"""
x=(1,2,6,4,9)
print(x)
n=x.index(6)
print("Index of 6:",n)

"""
#6
"""
fruits=("or","ap","ch","gr")
n=input("enter a fruit:")
x=fruits.index(n)
print("fruit",n,"is existed in position",x+1,"in the list")

"""
#7
"""
mark=(s1,s2,s3,s4,s5,s6,s7,s8)
(20,30,*50)=mark
print(30)

"""
#8
"""
x=(1,2,3,4)
y=("a","b","c")
z=x+y
print("Tuple 1:",x)
print("Tuple 2:",y)
print("Concatinated tuple:",z)

"""
#9
"""
x=(9,5,6,3,1,2)
print(x)
m=max(x)
n=min(x)
print("Max value:",m)
print("Min value:",n)

"""
#10
"""
x=(1,2,"a","b","c")
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

"""
#11

x=(("a",2),("b",4),("c",6),("d",1))
print(x)
n=max(x)
print(n)

#12
"""
x=(("a","cs",2000),("b","ec",3000),("c","me",1000))
m=max(x)
print(m)
n=m[0]
print("Employee with high salary:",n)

"""