## authored by Shane Dooley
#python getJGIgenomes.py $JGI_Export_File $Job_Error_Filename 
## 1. obtain an account from img.jgi.doe.gov/m/
## 2. change the username and password in the getJGIgenomes.py
## 3. From IMG browser, select all the genomes you want, add to cart, check the field "IMG Genome ID" to be included in the dispaly, and lastly import the excel sheet.
## 4. Open the file in excel and make IMG Genome ID as the first column, save the file as a tab-delimted text file, say JGIgenomelist.txt.
## 5. cmd: python getJGIgenomes.py JGIgenomelist.txt errlog.txt


import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import http.cookiejar
import sys
import os

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
post = urllib.parse.urlencode({'login':'fyang@iastate.edu',
                         'password':sys.argv[1],
                         'utf8':'%E2%9C%93',
                         'commit':'Sign+In'})
response = opener.open('https://signon.jgi.doe.gov/signon/create', post)
cookie.save(ignore_discard=True, ignore_expires=True)
#response = opener.open('https://signon.jgi.doe.gov/contact_updated')

IMG_File = open(sys.argv[2],"r")
errorFile = open(sys.argv[3],"w")
header = next(IMG_File)
header = header.strip()
header = header.split('\t')
listSize = 32000 #Temp variable just to keep track of where the download process is
for line in IMG_File:
  line = line.strip()
  lineArr = line.split(':')
  folderName = "IMG_" + lineArr[0].strip().split("_")[1]
  if os.path.exists(folderName):
	print("%s already exists, skip" %(folderName))
	errorFile.write("%s already exists, skip\n" %(folderName))
        continue
  os.mkdir(folderName)

  infoFileName = folderName+"/"+folderName+".info"
  infoFileHandle = open(infoFileName,'w')
  for i in range(0,len(lineArr)):
    infoFileHandle.write(header[i]+": "+ lineArr[i] + "\n")
  infoFileHandle.close()
  try:
    response = opener.open('http://genome.jgi.doe.gov/ext-api/downloads/get-directory?organism=IMG_'+lineArr[0])
    if(response.read().find("download_bundle.tar.gz") == -1):
      os.system("rm -rf " + folderName)
      errorFile.write(folderName+": "+ "download bundle not found\n")
      continue
  except Exception as e:
    os.system("rm -rf " + folderName)
    errorFile.write(folderName+": "+ str(e)+ "\n")
    continue
    
  downloadResponse = opener.open('http://genome.jgi.doe.gov/'+folderName+'/download/download_bundle.tar.gz')
  saveDownloadbundle = open(folderName+"/"+folderName+"_downloadbundle.tar.gz","w")
  saveDownloadbundle.write(downloadResponse.read())
  print("Completed Downloading: %s %.2f" % (folderName,(float(len(os.listdir("./")))/listSize)*100))
  #urllib2.HTTPError
#response = opener.open('http://genome.jgi.doe.gov/ext-api/downloads/get-directory?organism=IMG_638154510')
#print response.read()

#savefile = open('cookieresult.gz', 'w')
#savefile.write(response.read())
