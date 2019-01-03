#!/usr/bin/python
'''
    File name: v2pc-channel-status.py
    Author: Lakshman Savadamuthu
    Org: Cisco Solution/DevOps Support
    Date created: 12/04/2018
    Date last modified: 12/04/2018
'''
import sys
import json
from urllib import urlopen
import urllib
import dateutil.parser

def usage():
	if (len(sys.argv) < 3 or len(sys.argv) > 3):
  		print '''
    Usage: %s <AM node IP>  <workflow name>

    Check status of all channels within the workflow

    Parameters
    ----------

    <AM node IP or AM FQDN>
      AM node IP or FQDN if resolvable to pull data

    <workflow name>
      Workflow in which the channel line up is associated with


This script will compare two files for something
and print out matches

Usage:  theScript firstfile secondfile
'''
  		sys.exit(1)

#check the arg count
if len(sys.argv) < 2:
	usage()
print "Argument length is : " + str(len(sys.argv)) 
print "Argument 0 is : " + sys.argv[0]
print "Argument 1 is : " + sys.argv[1]
print "Argument 2 is : " + sys.argv[2]
#print "Argument 3 is : " + sys.argv[3]
amip = sys.argv[1]
workflow = sys.argv[2]

url = "https://{0}:7001/v1/assetworkflows/{1}/assets".format(amip,workflow)
#url = "https://live-am.v2pcops.com:7001/v1/assetworkflows/live1/assets/"

url = urlopen(url).read()
result = json.loads(url)
#unset https_proxy
for data in result:
   print '\n"Name":', data['contentId']
   print '\n"Status":', data['status'] ['state']
   captureengine = str(data['status']['captureStatus'][0]['captureEngine'])
   print '\n"Capture Engine":', captureengine
   print '"================================================================"'


Usage: python captures-details.py 200.8.0.46 live1
