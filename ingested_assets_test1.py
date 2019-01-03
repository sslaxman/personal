import json
from urllib import urlopen
import urllib
import dateutil.parser

for i in range(1,10):
	url="https://am-live-ce1-ums-0-1.mos1.cisco.com:7001/v1/assetworkflows/live/assets/CiscoTest"+str(i)
	url = urlopen(url).read()
	result = json.loads(url)  # result is now a dict
	Contentid=result['contentId']
	Status=result['status'] ['state']
	print '"================================================================"'
	print '"Content-id":', Contentid
	#print '"Status":', Status
	#ingeststart = dateutil.parser.parse(result['status']['startTime'])
	#ingestend = dateutil.parser.parse(result['status']['endTime'])
	capturestatus = result['status']['captureStatus']
	#captureengine = str(result['status']['captureStatus']['0']['captureEngine'])
	#print '"ingest-start time":', ingeststart
	#print '"ingest-end time":', ingestend
	#ingestduration = ingestend - ingeststart
	#print '"Ingest duration ":', ingestduration
	#print '"Capture Engine":', captureengine
	print '"Capture Status":', capturestatus
print '"================================================================"'
