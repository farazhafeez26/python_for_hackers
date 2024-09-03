
#3rd Sept - Sys 
import sys

print (sys.version)
print (sys.executable)
print (sys.platform)

'''
for line in sys.stdin:
	if line.strip()=="exit": 
		break
	sys.stdout.write (">> {}".format(line))
'''


for i in range (1,5):
	sys.stdout.write(str(i))
	sys.stdout.flush() 


for i in range (1,5):
	print(i)


'''
import time

for i in range (0,51):
	time.sleep(0.1)
	sys.stdout.write("{} [{}{}]".format(i, '#'*i, "."*(50-i)))
	sys.stdout.flush()
	sys.stdout.write("\n")

'''
'''
print(sys.argv)  #print the name of the script

if len(sys.argv)!=3: 
	print("[x] To run {} Enter a username and password.format(argv[0])") 

username=sys.argv[1]
password=sys.argv[2]

print("{} {}".format(username,password))

print(sys.path)
print(sys.modules)

'''

print(sys.argv)  #print the name of the script

if len(sys.argv)!=3: 
	print("[x] To run {} Enter a username and password.format(argv[0])") 
	sys.exit(5)

username=sys.argv[1]
password=sys.argv[2]

print("{} {}".format(username,password))

sys.exit(0)

#print(sys.path) #python will search for modules to be installed 
#print(sys.modules) #modulés that are already installed 



#26th Aug  - Xcomprehensions, Lambdas, functions


print("++++++++++++++++++++++++++++++++++")

#LAMBDAS 

add_4= lambda x : x +4 
print(add_4(4))

addd =lambda x,y: x+y 
print(addd(4, 6))



print((lambda x,y: x*y)(10,4))



is_even = lambda x: x % 2 ==0
print(is_even(2))
print(is_even(3))




blocks=lambda x,y: [x[i:i+y]for i in range(0, len(x),y)]

print(blocks("string",2)) 




to_ord = lambda x : [ord(i) for i in x]
print(to_ord("ABCD"))   

#nord returns the integer representation of each character. 


def to_ord2(x):
	list1=[]
	for i in x: 
		list1.append(ord(i))
	return list1

print(to_ord2("ABCD"))



print("++++++++++++++++++++++++++++++++++")

#functions

def function2(s):
	print("\t{}".format(s))

function2("parameter")



def function6(s1, *more):   # multiple arguments
	print("{} {}".format(s1, " ".join([s for s in more])))

function6("function6")
function6("jack", "ally", "b", "c")


#to print a dictionary of arguments

def function7(**ks): 
	for a in ks: 
		print(a, ks[a])

function7(a='1', b="2", c="3")		


def function8 (s,f,i,l):
	print(type(s))
	print(type(f))
	print(type(i))
	print(type(l))


function8("string",1.0, 1, ['l', 'i'])


v=100

def function9(): 
	global v
	v+=1 
	print(v)

function9()

print(v)

#---------------------

#call the function itself

def function12(x):
	print(x)
	if  x >0: 
		function12(x-1)   # recursive output

function12(5)


print("++++++++++++++++++++++++++++++++++")

#comprehensions
list1 = ['a','b','c']

print(list1)

list2= [x for x in list1]

print(list2)

list3 = [x for x in list1 if x  == 'a']
print(list3)

list5 =[hex(x) for x in range(5)]
print(list5)

list6= [hex(x) if x >0 else "x" for x in range(5)]
print(list6)

list7=[ x * x for x in range(5)]
print(list7)

list8 =[x for x in range(5) if x ==0 or x==1]
print(list8)


list9=[[1,2,3],[4,5,6],[7,8,9]]
print(list9)


list10 = [y for x in list9 for y in x ]
print(list10)

set1 = {x+x for x in range (5)}
print(set1)

list11 = [c for c in "string"]
print(list11)

print("".join(list11))
print("-".join(list11))

list12=[]
for c in "string":
	list12.append(c)
print(list12) 



#22nd Aug

#exception error and handling 
# exeptions can be handled by using try catch block 


#arthimetics errors, syntax errors and indentetnation eroors  

try:
	f = open("Dasads")
except:
	print("the junk doesnt exists  ")


print("------------")

try:
	f = open("Dasads") 
except Exception as e:
	print(e)


print("------------")


try:
	f = open("Dasads") 
except FileNotFoundError:
	print("the file does not exist! ")
except Exception as e:
	print(e)



print("------------")

 
try:
	f = open("top100") 
except FileNotFoundError:   # if there is not filenotfound error then it will go to the next exception 
 	print("the file does not exist! ")
except Exception as e:
	print(e)
finally: 
	print("this message!")

print("----Rasining exceptions--------")

'''n=100 
if n ==0: 
	raise Exception("n cant be 0")

print(1/n)	    #it will continue with the calculation

'''
print("------------")

'''n=0 
if n ==0: 
	raise Exception("n cant be 0")

print(1/n)	    #it will not continue with the calculation
'''

'''
n="aads"

if type(n) is not int:
	raise Exception ("n must be an int!") 

print(1/n)  # it could calculate 

'''

#assertion are sanity check  for hard error checking

b=1 	
assert(b !=0)
print(1/b)




# read and write file 

f=open ('top100')
print(f)

f = open ('top100', 'rt')   #rt read text 
print(f)

#r is read, w is write 

print(f.read())   #print the entire file as a string

print("---------")

f.seek(0)  

print(f.read()) 


# print(f.readlines())       #readlines are print array containing each line from the file. 

print(f.readlines()) # you will get [] which means the lines have been read. 

f.seek(0)   # start from 0 bytes

print(f.readlines())

f.seek(0)

for line in f: 
	print(line.strip()) #remove special characters
f.close()



print("---------")

f=open('write.txt', 'w')
f.write("Testline")
f.close()


f=open('write.txt','a')
f.write("testline2")
f.close()

print(f.name)
print(f.closed)
print(f.mode)

with open('top100') as f: 
	for line in f: 
		print(line)


#user input 
'''
test = input("Enter the IP:")
print(test)'''

while True:  #infinite loop
	test=input("Enter the ip address: ")
	print(">>> {}".format(test))
	if test =="exit":
		break
	else:
		print("exploiting..")






#sets  
#dont allow duplicate values 


print("--------------------")
set1={"a","b","c"}
print(type(set1))

set2={"a","a","a"}
print(set2	)

set3={"a", 0, True}
set4={"b",1, False}


set3.update(set4)   # true will replace 1 because no duplicate values

print(set3)

print(set2)

set1.add("d")

set4.update(lists1) # set4.discard4(4)
print(set4)

set4.add("j")

set4.remove("a")

print(set4)

#set1.pop()  

#set are ideal when we dont care about the order and the values 

#loops and conditionals
print("1>=1") if 1>=1 else print ("1 < 1")

if 1>=1:
	print("1>=1")
else: 
	print("1<1")

#nested loop 
for i in range(3):
	for j in range(3):
		print(i,j)

print("---------")

for i in range(5): 
	if i ==2:
		break
	print(i)
print("---------")

for i in range (5):
	if i==2: 
		continue
	print(i)


for i in range (5): 
	if i==2: 
		pass 
	print(i)


for c in "string": 
	print(c)

for key, value in {"a":1, "b":2, "c":3}.items():
	print(key, value)

for key  in {"a":1, "b":2, "c":3}.keys():
	print(key)


for value  in {"a":1, "b":2, "c":3}.values():
	print(value)

#21st Aug 
#bitwise operations
'''
print ((10<9)==True)
print((10==10)==True)
print(10>9)




print (10/3)
print(10//3)
print(10**10) # 10 to the power of 10
print(10 % 10) # prints the remainder   
print(10 % 3)


x =13 
print (bin (x))
print(bin(x)[2:].rjust(8,"0")) #adds zeros 

y= 5  
print(bin(y))
print(bin(y)[2:0].rjust(4,"0"))

print("----------")
print(bin(x & y)[2:].rjust(4,"0")) 

print(x&y)

print(bin(x |y )[2:].rjust(4,"0") )		

print(x | y)

print(bin (x >> 1) [2:].rjust(4,"0"))   #shift 1s to the right side. 

'''



#19th Aug 
'''
string= "am  a string!"
string2 = "I am \" \n m  a string"


print(string2)
print ("neut" in string2)

print(string2.startswith("I"))
print(string2.endswith("g"))
print(string2.split())

print (string2.encode())
print(string2.encode("utf-8"))

print(string2.rjust(25)) 

print(string2  .rjust(25,"x")) 

print("string2 is {} characters long!".format(len(string2)))

print("{} {}".format(1,2))
print("{} {}".format("a","b"))
print("The length is {length}".format(length=len(string2)))

length=len(string2)
print(f"the new length is {length}")
print(f"the new length is {length:.2f}")
print(f"the new length is {length:x}")  # hex
print(f"the new length is {length:b}")   #binary
print(f"the new length is {length:o}")     #octal


print("string is %d characters long!" % len(string2))     

'''

# the python interpreter in kali linux 
'''python       
Python 3.11.9 (main, Apr 10 2024, 13:16:36) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
>>>  exit () 

man python3

# executing inline python with opening the interprets 
python3 -c 'print("hello world")'

python3  -c  'import pty; pyt.spawn("/bin/bash");'

'''
'''
Step-by-Step Guide to Install Sublime Text on Kali Linux:

1. Added the GPG Key:

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

2. Ensured apt is set up to work with HTTPS sources:

sudo apt-get install apt-transport-https

3. Selected the Channel to Use:


echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

4. Updated apt sources and install Sublime Text:

sudo apt-get update
sudo apt-get install sublime-text

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
#8th Aug - Rebrushed the basics - Variables & data types
'''def test():
	print("test")

	string = "string"
	number = 10


test()

x= 1+2 + 3

print(x)

#https://docs.python.org/3/
#https://peps.python.org/pep-0008/

name="neut"
print(name)
name_length= 4 
print(name_length)

name, name_length="neut", 4

print(type(name))
print(type(name_length))


this_list=["ubuntu","linux","windows"]
this_tuple=("jack","jill")
this_dictionary={"keyboard":3, "pcs":5}

name_bytes=b"neut"
print(type(name_bytes))

print(this_list)
print(this_tuple)
print(this_dictionary)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''