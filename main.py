#OPERATORS

#ARITHEMATIC OPERATORS

#ADD
print(5+6)

#MINUS
print(22-89)

#MULTIPLY
print(5*6)

#DIVIDE
print(7/2)

#FLOOR dIVISION
print(7//2)

#REMAINDER
print(50%4)

#EXPONENT
print(7**2)

#Comparsion OPERATORS

#less than
x=10
y=30
Res=x<y
print(Res)

#less than equal to
x=10
y=30
Res=x<=y
print(Res)

#Greater  than
x=10
y=30
Res=x>y
print(Res)

#Greater than equal to
x=10
y=30
Res=x>=y
print(Res)

#equal to
x=10
y=30
Res=x==y
print(Res)

# Not equal to
x=10
y=30
Res=x!=y
print(Res)

#logical Operator

#And
x,y=34,56
a,b=78,98
res=(x>a)and(y>b)
print(res)

#Or
x,y=34,56
a,b=78,98
res=(x>a)or(y>b)
print(res)

#Not
x,y=34,56
a,b=78,98
res=not(x>a)
print(res)

#Asiignment Operator

#=
n1,n2=89,54
sum=n1+n2
print(sum)

#+=
n1+=10
print(n1)

#-=
n1-=20
print(n1)

#/=
n1/=10
print(n1)

#%=
n1%=10
print(n1)

#//=
n1//=10
print(n1)

#**=
n1**=10
print(n1)

#BITWISE OPERATOR

#>>
res=14>>2
print(res)

#<<
res=14<<2
print(res)

#&
res=14&2
print(res)

#|
res=14|2
print(res)

#^
res=14^2
print(res)

#IDENTITY OPERATOR

#IS
a=[23,45,67]
b=[23,45,67]
if (a is b):
    print("Same identity")

#IS NOT
c=[23,45,67]
if (b is not c):
    print(" not Same identity")

#MEMBERSHIP OPERATOR

#IN
str="VineetKumar"
if("Kum" in str):
    print("available")
else:
    print(" not available")

#NOT IN
if("War" in str):
    print("available")
else:
    print(" not available")