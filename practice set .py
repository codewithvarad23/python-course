# List Data type methods

# 1 sorted() method  it is return new list

G1=["Apple","Banana","Orange"]
result=sorted(G1)
print(result)

print('\n')
# sort() method it is modify the list 


G2=[2,54,3,64,3,6]
print(G2)
r1=G2.sort()
print(G2)

print('\n')

# append() it is used to add new elements

H1=['Karan','varun','kartik','sham']
r2='udayraj'
H1.append(r2)
print(H1)


print('\n')
# for loop in python 
num=[1,2,3,4,5,6]
for x in num:
    print(x)


print('\n')

# for loop and range type used
for c in range(1,11):
   p=c*3
   print(p)

print('\n')

for x in range(10,0,-1):
    pr=x*4
    print(pr)



# program second largest number find using sorted and slicing

list1=[200,353,2646,855,895,7000]
r=sorted(list1)
r_f=r[-2]
print(r_f)


# sum() method

User=[1,2,3,4,5]
r_u=sum(User)
print(r_u)


# copy() method

a1=["Apple","orange","banana"]
a2=a1.copy()
print(a2)


# program find sum of no in list

num1=[1,2,3,4,5]
print(sum(num1))
# find sum using for loop
sum=0
for i in num1:
  sum=sum+i
print(sum)
    


