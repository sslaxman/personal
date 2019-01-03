import json
from urllib import urlopen
import urllib
import dateutil.parser

for i in range(1,2):
	#url="https://vod-am.v2pcops.com:7001/v1/assetworkflows/vod1/assets/VOD_2hrs"
	url="https://vod-am.v2pcops.com:7001/v1/assetworkflows/vod1/assets/2hrs_movie1"
	url = urlopen(url).read()
	result = json.loads(url)  # result is now a dict
	Contentid=result['contentId']
	Status=result['status'] ['state']
	print '"================================================================"'
	print '\n"Content-id":', Contentid
	print '\n"Status":', Status
	ingeststart = dateutil.parser.parse(result['status']['startTime'])
	ingestend = dateutil.parser.parse(result['status']['endTime'])
	#capturestatus = result['status']['captureStatus']['state']
	captureengine = str(result['status']['captureStatus'][0]['captureEngine'])
	print '\n"ingest-start time":', ingeststart
	print '\n"ingest-end time":', ingestend
	ingestduration = ingestend - ingeststart
	print '\n"Ingest duration ":', ingestduration
	print '\n"Capture Engine":', captureengine
	#print '\n"Capture Status":', capturestatus
print '\n"================================================================"'
