# Kuldeep Singh Sidhu
# github.com/singhsidhukuldeep


#importing dependencies
from urllib.request import urlopen as uReq #for opening URLs
from bs4 import BeautifulSoup as soup #for screaping the web

my_url = "http://football-data.co.uk/englandm.php" #URL you want to scrap

uClient = uReq(my_url) #opening connection and grabing the page
page_html = uClient.read() #reading the page
uClient.close() #closing the connection

#parsing as html (can be xml,etc.)
page_soup = soup(page_html, "html.parser") 

#grabing all <A> tags
aAll = page_soup.findAll("a")

allDownloadLinks = [] #Creating a list of all the links
counterAllDownloadLinks = 0 #counting number of links

#going through all <A> tags
for a in aAll:
	link = a["href"] #getting the href attribute or the URL

	#getting URLs with the dataset
	if "mmz4281/" in link:
		counterAllDownloadLinks += 1 #increasing the counter

		link = "http://football-data.co.uk/" + link #completing the link for usage
		print (str(counterAllDownloadLinks) + ":\t" + link)
		allDownloadLinks.append(link) #Adding to the list

#Seperating different leagues
premiereLeagueDownloadLinks = []
championshipDownloadLinks = []
league1DownloadLinks = []
league2DownloadLinks = []
conferenceDownloadLinks = []

for links in allDownloadLinks:
	if "E0" in links:
		premiereLeagueDownloadLinks.append(links)

	elif "E1" in links:
		championshipDownloadLinks.append(links)

	elif "E2" in links:
		league1DownloadLinks.append(links)

	elif "E3" in links:
		league2DownloadLinks.append(links)

	elif "EC" in links:
		conferenceDownloadLinks.append(links)

#Writing the links to files
checkWrite = input ("\n\nDo you want to create files for the Download Urls [Y/N]: ")

if any(x in checkWrite for x in ('Y', 'y')):

	file = open("AllDownloadLinks.txt","w")
	for link in allDownloadLinks:
		file.write(link)
		file.write("\n")
	file.close()

	file = open("PremiereLeagueDownloadLinks.txt","w")
	for link in premiereLeagueDownloadLinks:
		file.write(link)
		file.write("\n")
	file.close()

	file = open("ChampionshipDownloadLinks.txt","w")
	for link in championshipDownloadLinks:
		file.write(link)
		file.write("\n")
	file.close()

	file = open("League1DownloadLinks.txt","w")
	for link in league1DownloadLinks:
		file.write(link)
		file.write("\n")
	file.close()

	file = open("League2DownloadLinks.txt","w")
	for link in league2DownloadLinks:
		file.write(link)
		file.write("\n")
	file.close()

	file = open("ConferenceDownloadLinks.txt","w")
	for link in conferenceDownloadLinks:
		file.write(link)
		file.write("\n")
	file.close()


	print ("\n\n\n6 Files have been created:\n\n1:\tAllDownloadLinks.txt\n2:\tPremiereLeagueDownloadLinks.txt\n3:\tChampionshipDownloadLinks.txt\n4:\tLeague1DownloadLinks.txt\n5:\tLeague2DownloadLinks.txt\n6:\tConferenceDownloadLinks.txt\n")
