# -*-coding:utf-8-*-

import urllib,httplib
from BeautifulSoup import BeautifulSoup
import re
import os
from flask import Flask

url = '192.168.168.168'


app = Flask(__name__)
	

def login(url,userid,passw):
	print passw
	postp= {'R6': 1, 'DDDDD': userid, 'upass': passw,'0MKKey': '%B5%C7%A1%A1%C2%BC'}
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


@app.route('/')
def wifi_login():
	url = '192.168.168.168'
	onePwd = '034069'
	userid = '101002013030200'
	login(url,userid,onePwd)
	return 'wifi Login success!'
	

# net_status = os.system('ping git.neo0.xyz')
# if net_status:
# if login(url,userid,onePwd):
	# print 'success!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=80)

