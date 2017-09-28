# Kuldeep Singh Sidhu
# github.com/singhsidhukuldeep


from urllib import request as uReq



def downloadFile (url):
	urlOpen = uReq.urlopen(url)
	urlRead = urlOpen.read()
	downloadStr = str(urlRead)

	downloadStrLines = downloadStr.split("\\n")

	downloadFileName = url.split("/")[-1]

	downloadStrLength = len(downloadStrLines)
	progress = 100/downloadStrLength
	perProgress = 0

	fx = open (downloadFileName , "w")
	for downloadStrLine in downloadStrLines:
		fx.write(downloadStrLine + "\n")
		perProgress += progress
		print (perProgress)
		print ("#"*int(perProgress/5)+"\n")
	print ("---------Download Finished----------")



'''
file_name = url.split('/')[-1]
u = uReq(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print ("Downloading: %s Bytes: %s" % (file_name, file_size))

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print (status,)

f.close()''' 