#!/usr/bin/env python2.7

'''
Script to monitor number of qsub jobs every 30 seconds. Useful when cluster only admits
a certain number of jobs per user. You need to define the username, otherwise just run as:

python monitorqsub.py

@author: Moises Exposito-Alonso (moisesexpositoalonso@gmail.com)

'''


import subprocess, time


totjobs=1
while totjobs >=1:
	try:
		res=subprocess.check_output(['q-charge', '--user=mexposito', '--no-summary' ,'--no-globals'])  
		#res=subprocess.check_output(['qstat' ,'-u' ,'mexposito' ] ) 
                #print(res)
		res=[x for x in res.split("\n")]
                totjobs=res[1][-1]

		print totjobs
		time.sleep(0.5)
	except KeyboardInterrupt:
		raise

