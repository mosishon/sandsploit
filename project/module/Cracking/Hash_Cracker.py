#!/usr/bin/python3
import hashlib,sys

sys.path.append("/data/data/com.termux/files/usr/opt/sandsploit/core")
sys.path.append("/opt/sandsploit/core/")
import complator
HASH = None
TYPE_HASH =None
PASSLIST = None
name = "Hash Cracker"
author = "@Aμιρ-0x0 (AMJ)"
info = "Tool for cracking hash codes."
def help():
    print ("author              to show author name")
    print ("help                to show this massage")
    print ("info                to show description of the tool ")
    print ("set                 to set options such as : [set host http://google.com/]")
    print ("show_options        to show options of Tools")
    print ("exit                to quit from Tool")
    print ("run                 to Run Session")
def options():
	
    print ("options               value")
    print ("==========            ============")
    print ("Hash                  ",HASH)
    print ("passlist              ",PASSLIST)
    print ("type_hash             ",TYPE_HASH)
    print (" ")
    print ("[*]-md5")
    print ("[*]-sha1")
    print ("[*]-sh224")
    print ("[*]-sha256")
    print ("[*]-sha384")
    print ("[*]-sha512")

def run():
	try:

		wordlist = open(passlist,"r").readlines()

		for password in wordlist:
			password = password.strip()

			if type_hash == "md5":
				hash_a = hashlib.md5(password).hexdigest()
			elif type_hash == "sha1":
				hash_a = hashlib.sha1(password).hexdigest()

			elif type_hash == "sha224":
				hash_a = hashlib.sha224(password).hexdigest()
			elif type_hash == "sha256":
				hash_a = hashlib.sha256(password).hexdigest()
			elif type_hash == "sha384":
				hash_a = hashlib.sha384(password).hexdigest()
			elif type_hash == "sha512":
				hash_a = hashlib.sha512(password).hexdigest()
			if hashing == hash_a:
				print ("[+] hash is cracked > ",password)
				break
			else:
				print ("[-] try test ",password)
	except:
		print ("Error! Please check Options ")

while True:
    try:
        option = input ("\033[96m┌─[SSF][\033[91m"+name+"\033[96m]\n└─▪ ")
        op2 = option.split(" ")
        if option == "help":
            help()
        elif option == "author":
            print (author)
        elif option == "info":
            print (info)

        elif option == "show_options":
            options()
        elif op2[0] == "set":
            op3 = op2[1].upper()    
            vars()[op3] = op2[2]
            print ("%s => %s"%(op2[1],op2[2]))
        elif option == "run":
            run()
        elif option == "exit":
            break
        else:
            print ("Wrong Command ! ")
    except:
        print ('Unkonwn Error !')