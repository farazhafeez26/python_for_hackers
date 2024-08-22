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