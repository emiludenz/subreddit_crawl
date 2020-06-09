from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib import request
from classes import *

"""
This crawler implementation is scraping HTML which is making unnecessarily harder for yourself.
You can access a JSONified version of each page by appending .json to any page URL
example https://www.reddit.com/r/datasets/comments/8c9f4j/i_have_implemented_a_crawler_for_reddit_data/.json
"""

def crawl(subreddit_url):
	"""Returns a list containing all threads on the subreddit page from the given reddit url
	Param url: url to the reddit site
	"""
	req = request.Request(subreddit_url, 
    	data=None, 
    	headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	})

	content = request.urlopen(req).read()
	threads_container = list()
	subreddit_name = subreddit_url.split("/")[-2]+".html"
	
	# Saving as html
	with open(subreddit_name,"w") as txt:	
		txt.writelines(str(content))

	with open(subreddit_name) as html:
		soup = BeautifulSoup(html,"html.parser")
		site_table = soup.find_all("div",{"id":"siteTable"})
		if site_table:
			site_table = site_table[0]
			# Find all threads, starting with thing_t3_
			threads = site_table.find_all('div', id=lambda x: x and x.startswith('thing_t3_'))
			if threads:
				for t in threads:
					# Skip commercials
					if t.find("span","sponsored-indicator rank"):
						continue
					# Users
					user = t["data-author"]
					# Links to reddit page
					link = t["data-permalink"]
					# Links to article
					article_link = t["data-url"]
					# Title of thread
					title = t.find("p",{"class":"title"}).contents[0].text
					#print("\n\n\n\n\n\n\n")
					threads_container.append(Thread(title, link, article_link, "r/scandinavia",user))
	
	return threads_container