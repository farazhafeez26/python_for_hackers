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