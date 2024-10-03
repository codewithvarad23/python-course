# program largest number  and small number find in list

lists=[909,232,53,43,743,636,243]
lergest=[]
small=[]
for x in lists:
    if x>100:
        lergest.append(x)
    else:
        small.append(x)
print(f'Largest number {lergest}')
print(f'small number {small}')



# program positive and negitive number find in list using for loop

num=[2,-43,3,35,0,-31,-88,-28]
print(num)
print('\n')
pos=[]
neg=[]
for v in num:
    if v>0:
        pos.append(v)
    else:
        neg.append(v)
print(f'Positive numbers is {pos}')
print(f'Negitive numbers is {neg}')



# program 
A=['Apple','cherry','orange','banana']
print(A)
primt




# program validate age in car driving

age=[44,33,9,14,16,19,20]
drive=[]
notdrive=[]
for x in age:
    if(x>18):
        drive.append(x)
    else:
        notdrive.append(x)
print(f'Driving age {drive}')
print(f'Not Driving age {notdrive}')


# print the patten 

for x in range(1,6):
    a=x* ' * '
    print(a)

print('\n')
# reverse print the patten

for x in range(5,0,-1):
    b=x*' * '
    print(b)



# print a 