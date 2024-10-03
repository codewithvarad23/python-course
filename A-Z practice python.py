# list method 

# extend()

p=[4,3,4,5]
p2=[1,2,3]
p2.extend(p)
print(p2)


# copy()

a=['apple','orange','watermolen']
a1=a.copy()
print(a)
print(a1)

# reverse()

re=[1,2,34,5]
re.reverse()
print(re)



# program insert()
name=['dhanjay','amol','kartik']
name.insert(0,'Harsh')
print(name)

# remove()

k=[1,2,4,5]
k.remove(5) # value or element
print(k)


# clear()
s=[1,3,5,7,8]
s.clear()
print(s)



# count()

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
print(x)




t=(100,233,898,938,63,82,37)
for x in t:
    if x >100:
        print(f'largest numbers {x}')
    else :
        print(f'small numbers {x}')
        