# program to check the data type of a given variable.

a='Hello world'
print(type(a))
type(a)

# program to input a string and convert it to an integer, then print the result

UserInput= input('Enter your Number')
convert=int(UserInput)
print(convert)

# program to concatenate an integer and a string after converting the integer to a string.

Integ=90
covertstr=str(Integ)
print(covertstr)

# program to input a string and find its length.

uservalue=input("Enter Your Name")
find= len(uservalue)
print(find)

# program to input a float value, convert it to an integer, and print the result.

UserInput= input('Enter your Number')
convert=int(float(UserInput))
print(convert)

# program to input two float numbers, add them, and print the result.

Usernum=float(input('Enter Your Number'))
Usernum2=float(input('Enter Your Number'))
Sum=Usernum+Usernum2
print(Sum)

# program to check if a given string is numeric.

uservalue=input("Enter Your Name")
find= uservalue.isnumeric()
print(find)


# program to convert a list of numbers to a tuple.

num=[1,2,3,4,5]
result=tuple(num)
print(result)

# program to input a string of numbers, extract each digit, convert them to integers, and find their sum.

numb=input("enter your number")
digits=list(numb)
ad=sum(map(int,digits))
print(ad)

# program to concatenate a list and a tuple, after converting the tuple to a list.

lists = [1, 2, 3]
tuples = (4, 5, 6)
add= list(tuples)
converts =lists + add

print(converts)


#  lenght program

strings="The Baap Company"
print(strings)

print(len(strings))

# slice program

a="Baap"
b=a[:1]
print(b)

# slice program
# any position
a="Baap"
b=a[0:2]
print(b)

# program second 3 charater
a="Baap"
b=a[1:3]
print(b)

# starting position index zero
a="Baap"
b=a[:3]
print(b)

print(a[1:2]) #
print(a[1])

# one by one word prints

print(a[0])
print(a[1])
print(a[2])
print(a[3])

# program reverse words
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[::-1])

# last word print only
print(a[3:4]) # index no
print(a[3]) # slice


# last 2 word print only
print(a[::-2])


print(a[0::2])# print only B-A

b='Company'
print(b)
print(b[0:7:3])
# print only CPY


print(b[0:7:6]) # print only cy
print (b[4:7]) # print only any

# reverse print
print(b[::-1])
print(b[-1:-5:-2]) # Yn
print(b[-1:-5:-1]) # y n a p word prints only

# program string  len() method
a="hello , world"
print(len(a))

# reverse print
print(a[::-1])


# only last word print
print(a[-1])

# reverse()
# slice()
# len()

# program uppercase()

print(a.upper())

# Lowercase()
print(a.lower())

#
st="hello world "
print(st*3)

# program using strip() method
t="     hi   guys "
print(t.strip())

g="The Baap Company"
print(g.split())
print(len(g))
print(g[::-1])
print(g.upper())
print(g.lower())

# Program replace()
print(g.replace("Baap","Company"))

# program lower to upper
m="Master of computer Application"
print(m)
print(m.upper())

print(m.replace("Master","A"))

# Lower convert
v="The developer"
print(v.lower())


# program add two value in one variable
x="Baap"
y="company"
x=x + " " + y
print(x)

# format string

name="The Baap Company"
print(f"company name is {name}")

live="Gangapur"
p=int(349322)
print(live,p)

# 4 sentence print

Myname="varad"
SName="Pandit"
Phone=9382993743
Educate="MCA"
print(f" my name is {Myname} {SName} my phone no {Phone} My Education {Educate}")



# String Methods
# Capitalize program

H="the Baap Company"
print(H.capitalize())

# casefold() Converts string into lower case

a1="The Baap Company"
print(a1.casefold())

# center() Returns a centered string
print(a1.center(60))

# count() Returns the number of times a specified value occurs in a string
print(a1.count("a"))

# encode()	Returns an encoded version of the string
k="The Baap Company"
print(k.encode())

# endswith()	Returns true if the string ends with the specified value
print(k.endswith("y"))

# expandtabs()	Sets the tab size of the string
c="V\ta\tr\ta\tr\td"
print(c.expandtabs(5))

# find()	Searches the string for a specified value and returns the position of where it was found
print(c.find("world"))

# format()	Formats specified values in a string
nu="The software"
print(nu.format())

# format_map()	Formats specified values in a string
f="The Baap Company"
print(f.format_map("C"))


# index()	Searches the string for a specified value and returns the position of where it was found

print(f.index("C"))


# isalnum()	Returns True if all characters in the string are alphanumeric
print(f.isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
g="TheBaapCompany"
print(g.isalpha())

# isascii()	Returns True if all characters in the string are ascii characters
print(g.isascii())

# isdecimal()	Returns True if all characters in the string are decimals
print(g.isdecimal())


# isdigit()	Returns True if all characters in the string are digits
print(g.isdigit())

# isidentifier()	Returns True if the string is an identifier
he="The developer"
print(he.isidentifier())

# islower()	Returns True if all characters in the string are lower case
print(he.islower())

# isnumeric()	Returns True if all characters in the string are numeric
na="123456"
print(na.isnumeric())

# isprintable()	Returns True if all characters in the string are printable
n1="Good Morning"
print(n1.isprintable())

# isspace()	Returns True if all characters in the string are whitespaces
print(n1.isspace())


# istitle()	Returns True if the string follows the rules of a title
print(n1.istitle())

# isupper()	Returns True if all characters in the string are upper case
s="I AM GOOD"
print(s.isupper())

# join()	Joins the elements of an iterable to the end of the string
k="Sad"
k8="Happy"
print(k8.join(k))

# ljust()	Returns a left justified version of the string
print(s.ljust(20))

# lower()	Converts a string into lower case
print(s.lower())

# lstrip()	Returns a left trim version of the string
B1="   The Developer  "
print(B1.lstrip())

# maketrans()	Returns a translation table to be used in translations
B2="THE"
print(B2.maketrans("T","t"))

# partition()	Returns a tuple where the string is parted into three parts
print(B2.partition("T"))

# replace()	Returns a string where a specified value is replaced with a specified value
Name="Sandeep"
print(Name.replace("S","M"))

# rfind()	Searches the string for a specified value and returns the last position of where it was found
print(Name.rfind("p"))

# rindex()	Searches the string for a specified value and returns the last position of where it was found
print(Name.rindex("n"))

# rjust()	Returns a right justified version of the string
print(Name.rjust(10))


# rpartition()	Returns a tuple where the string is parted into three parts
print(Name.rpartition("a"))

# rsplit()	Splits the string at the specified separator, and returns a list
h2="The Baap Company"
print(h2.rsplit())

# rstrip()	Returns a right trim version of the string
print(h2.rstrip())

# split()	Splits the string at the specified separator, and returns a list
k1="Hello       Guys"
print(k1.split())

# splitlines()	Splits the string at line breaks and returns a list
print(k1.splitlines())

# startswith()	Returns true if the string starts with the specified value
b4="Hey I am"
print(b4.startswith("H"))

# strip()	Returns a trimmed version of the string
h5="    The Baap Company    "
print(h5.strip())

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
print(h5.swapcase())

# title()	Converts the first character of each word to upper case
p1="Good Morning"
print(p1.title())

# translate()	Returns a translated string
print(p1.translate("G"))

# upper()	Converts a string into upper case
print(p1.upper())


# zfill()	Fills the string with a specified number of 0 values at the beginning
num="123456"
print(num.zfill(10))

a="Hello, World!"
r=a[1:5].upper()
print(r)

a1=input("Enter Your Name")
b=a1[0:7]
print(b)

