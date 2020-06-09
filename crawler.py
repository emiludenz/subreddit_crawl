import site_crawl 
import thread_crawl
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
from classes import *
import time
import sys
import arg_checker



def main():
	url = arg_checker.check_args(len(sys.argv), sys.argv)
	try:
		threads = site_crawl.crawl(url)
		for t in threads:
			# To avoid sending to many requests to the server, 
			# the program will have to sleep for 15 seconds between each iteration
			time.sleep(15)
			comments = thread_crawl.crawl(t.thread_url)
			t.print_thread()
			for c in comments:
				c.print_comment()
	except urllib.error.HTTPError as h:
		print(h)
		exit(-1)
	exit(1)




if __name__ == '__main__':
	main()