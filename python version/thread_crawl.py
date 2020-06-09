from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib import request
from classes import *

def crawl(thread_url):
	"""Returns a list containing all comments from a reddit thread url 
	Param thread_url: url to the thread
	"""
	base_url = "https://np.reddit.com"
	comment_container = list()
	req = request.Request(base_url+thread_url, 
    	data=None, 
    	headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	})
	
	content = request.urlopen(req).read()
	thread_name = thread_url.split("/")[-2]+".html"

	# Saving as html
	with open(thread_name,"w") as txt:	
		txt.writelines(str(content))

	# Opening the html from disk
	with open(thread_name) as html:
		soup = BeautifulSoup(html, "html.parser")
		s = soup.find_all("div", {"class","content"})
		if s:
			s = s[0].find_all("div", id=lambda x: x and x.startswith('thing_t1_'))
			for _s in s:
				# Getting the user that has posted the comment
				user = _s["data-author"]
				
				# Getting the text of the comment
				text = _s.find("div", {"class":"md"}).text
				# Need to do replacements to get the correct output
				text = text.replace("\\xc3\\xa5","å").replace("\\xc3\\xb8","ø").replace("\\xc3\\xa6","æ")
				
				# Datetime for comment			
				time = _s.find("time", {"class":"live-timestamp"})
				time = time["datetime"]

				# Link to comment
				link = base_url+_s["data-permalink"]

				comment_container.append(Comment(user,text,time,link))

	return comment_container