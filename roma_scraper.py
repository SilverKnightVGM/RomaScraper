# This script scrapes info for the top games of all time sorted by metascore
import requests, os, re
from bs4 import BeautifulSoup
from time import sleep, time
from random import randint
import codecs

lines = []

def main():
	#These will help use measure how often we make requests
	requests = 0
	start_time = time()
	
    #txt file with a URL per line
	file_name = "links roma.txt"
	
    #Used to autonumber files, counts number of links in txt input file
	num_lines = sum(1 for line in open(file_name))
	padding = len(str(num_lines))
	
	print("Starting Now")
	
	with open(file_name, "r") as f:
		global lines
		lines = f.read().splitlines()
	
		for line in lines:
            #Get last part of url
			name = line.rfind("/")
			name = line[name+1:-5]
            #pad file name with auto-numbering
			name = str(requests).rjust(padding, "0") + "." + name
			
            getAndSaveContent(line, name)
			
            requests += 1
			
            #Don't send http requests too fast
            sleep(randint(1,3))
            
			elapsed_time = time() - start_time
			print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
		

# def renameFiles(name):
	# for idx, filename in enumerate(os.listdir("./result")):
		# prefix = os.path.join(os.getcwd(), "result")
		# os.rename(os.path.join(prefix, filename), os.path.join(prefix, name[idx]))

def getAndSaveContent(url, nameFile):
	hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }

	# Make the request
	page = requests.get(url, headers=hdr)

	# Create a BeautifulSoup object
	soup = BeautifulSoup(page.text, 'html.parser')

	# Selector for the main content
	article_content = str(soup.find('div', attrs={'class': 'post-body entry-content'}))

    #This writes the file with a UTF-8 BOM "utf-8-sig", use this to prevent weird problems with accented characters
    #The UTF-8 BOM is mostly used by Microsoft products to auto-detect the encoding of a file
    #https://stackoverflow.com/questions/23154355/python-utf-8-sig-bom-in-the-middle-of-the-file-when-appending-to-the-end
	with codecs.open(os.path.join("result", nameFile + '.html'), "w", "utf-8-sig") as output:
		output.write(article_content)

if __name__ == '__main__':
	main()
	# print()