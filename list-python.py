# What is a List?
# A list in Python is a mutable, ordered collection of elements. Lists can store elements of different data types like integers, strings, or even other lists.




# Lists are used to store multiple items in a single variable.

# Lists are created using square brackets:

# List items are ordered, changeable, and allow duplicate values.
# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

li=["apple","banana","charry"]
print(li)
print('\n')
type(li)



students=['abhay','sham','vikas','anand','govind']
print(students)

type(students)

# print first name
print(students[0])

# print 3d name
print(students[2])

# print last name
print(students[4])

# reverse print
print(students[::-1])

# print

studName=['Anand','sham','raj']
print(studName)


sn=['a','b','c','d','e','f'] # print only d, e, f
print(sn[3:6])

print(sn[1:3]) # print only b,c

s=sn.append('g') # add g in list
print(sn)

type(sn) # type check

x=sn.append('Baap company') # add the baap company or append()
print(sn)

print(sn[7]) # print only baap company


college=[100,200,300,'student','marks']
print(college)
print(college[3])
print(college[0:2])
print(college[0:5:2])
print(college[0:5:3])
print(college[1:5:2])
print(college[0:5:4])

a='company'
print(a)
type(a)

college[0]='baap'
print(college)
college[3]='student'
print(college)

result="".join(college.split())[0].append('Sham')
print(result)
print(college)

re=college.remove('student')
print(re)
print(college)

re=college.remove(200)
print(college)
res=college.append(2000)
print(college)

data=[True,'the',{'name':'varad'},("apple"),[1,2,3,4,5],1.2, 88, 3j, {'Aman','varun'}] # list print
print(data) # list is multiple data types

a=['a','b','c''d','e']
re=a.insert(0,'school') #insert program
print(a)



# Program list
l1=[21,23,37,84,95]

print(max(l1)) # maxium



l2=[333,2.3,599,333]
print(min(l2)) # minimum
print(max(l2))# max program list

#  sum() function or Method
l3=[1,2,3,4,5,6,7,8,9,10]
print(sum(l3))

# copy()
l4=l3.copy()
print(l4)

li=[3,35,7,"hi"]
print(li)
print(sum(li))

list1=[1,2,3] # sum
list2=[4,5,6]
lo=sum(list1+list2)
print(lo)
type(lo)

# sort() method
G1=[22,33,7,44,8,77]
print(G1)
G1.sort()
print(G1)

G2=[786,33,1000,44,8,77]# print 2nd lagest no
x=sorted(G2)
x[-2]
print(G2)


# small number print in variable
G3=[786,4000,10000,440,8,77]
x=sorted(G3)
print(x)
print(x[0])


# 3d lagest number in list
G3=[786,4000,10000,440,8,77]
x1=sorted(G3)
print(x1)
print(x1[-3])

# list -- for loop
G4=["apple",'banana','cherry','orange','kiwi']
print(G4)
for x in G4: # in means variable uder
    print(x)


# numbers print in for loop
nu=[1,2,3,4,5,6,7,8,9,10]
for x in nu:
    print(x)

# for loop
g7=[22,1.3, "hey",2200]
print(g7)
for x in g7:
    print(x)

n=[1,2,3,4,6]
for x in n:
    a=x*x
    print(a)

j=[1,2,3,4]
for x in j:
    p=x*x*x
    print(p)

# program list print
a1=['a','b','c','d']
print(a1)


# program find sum of no in list

num1=[1,2,3,4,5]
print(sum(num1))
# find sum using for loop
sum=0
for i in num1:
  sum=sum+i
print(sum)


# program to create list using range function
a=list(range(10))
print(a)

#  using for loop
l1=[]
for i in range(10):
    l1.append(i)
print(l1)



# user input program

UserInput=int(input("Enter the number:"))
print(UserInput)

x=input("Enter the value:")
print(x)

y=input("Enter the value:")
print(y)

# program input enter the name print
name=input("Enter the name:")
print(name)


company=input("Enter the company:")
print(company) # company name print program

# program addition of two no
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
c=a+b
print(c)

# program subtraction of two no
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
c=a-b
print(c)

# program multipltion
m1=int(input("Enter the 1st no:"))
m2=int(input("Enter the 2nd no:"))
m3=m1*m2
print(m3)

# program division of two numbers
d1=int(input("Enter the 1st no:"))
d2=int(input("Enter the 2nd no:"))
d3=d1/d2
print(d3)

# program %
a1=int(input("Enter the 1st no:"))
a2=int(input("Enter the 2nd no:"))
c=a1%a2
print(c)

# program square root
sq=[]
for i in range(1,11):
    sq.append(i*i)
print(sq)

# program to even or odd no
num=[1,2,3,4,5,6]
odd=[]
even=[]
for i in num:
    if i%2==0:
      even.append(i)
    else:
      odd.append(i)
print(even)
print(odd)


# program positive and negitive no
num1=[1,2,3,4,5,6 -33,-44,-5]
pos=[]
neg=[]
for i in num1:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
print(f'Positive Numbers {pos}')
print(f'Negitive Numbers {neg}')

# program lagest num and small no
num=[1000, 200,78,300,1,2,500,786,92]
lar=[]
sma=[]
for x in num:
  if x>100:
    lar.append(x)
  else:
    sma.append(x)
print(f'Largest number {lar}')
print(f'small number {sma}')

# program leap year using lf else
a=int(input("Enter the year:"))
if a%4==0:
    print("Leap year")
else:
    print("Not leap year")

# program user age
age=[18,20,17,16,14,1,30,40]
election=[]
non_election=[]
for x in age:
  if x>18:
    election.append(x)
  else:
    non_election.append(x)
print(f'Election select age {election}')
print(f'Non Election select age  {non_election}')


# program 5 table
num5=5
for i in range(1,11):
    print(num5*i)

n=10 #10 table print
for i in range(1,11):
    print(n*i)

# program palindrome words find

s=str(input("Enter the words:"))
if s==s[::-1]:
    print("is palindrome word")
else:
    print("not palindrome word")

# program patten print
num=5 #5 patten print
for i in range(1,6):
    print(i*' * ')

for x in range(6,0,-1):
    print(x*' * ')

tuples=('apple','banana','cherry')
print(tuples)
tuples.append('orange')
print(tuples)

# tuple program add two variable

t1=('apple','banana','cherry')
t2=('orange','kiwi','mango')
t3=t1+t2
print(t3)

for x in t3:
  print(x)

