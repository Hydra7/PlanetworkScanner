#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("data.txt","r");
	link = raw_input("Masukkan Link Website \nSet Target --> ")
	print "\n\nSedang Mencoba....\n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Dapat --> ",req_link
def Credit():
	Space(9); print "################################################"
	Space(9); print "#          PLANETWORK ADMIN SCANNER            #"
	Space(9); print "#             Recoded by : Hydra7              #"
	Space(9); print "#                  ----------                  #"
	Space(9); print "#          Dark-IT & PLANETWORK TeaM           #"
	Space(9); print "################################################"

Credit()
findAdmin()
