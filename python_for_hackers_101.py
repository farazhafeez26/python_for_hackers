
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