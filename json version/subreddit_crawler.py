#Getting page info with .json
from urllib.request import urlopen, Request
from urllib import request
import json
import os, sys
from classes import *
from datetime import datetime


def main():
	#subreddit_url = create_json_link_from_url("https://np.reddit.com/r/scandinavia")
	#page_name = get_page_name_from_url(subreddit_url)
	"""
	content = get_content_from_subreddit(subreddit_url)
	save_json_to_file(page_name, content)
	data = load_json_from_file(page_name)
	thread_container = get_threads_from_json_object(data)
	"""
	thread_url = "https://np.reddit.com/r/Denmark/comments/f303pn/sas_viking_ancestors/"#"https://np.reddit.com/r/scandinavia/comments/gzkpzb/risikerer_alle_danskere_der_har_videregivet.json"
	content = get_content_from_subreddit(thread_url)
	page_name = get_page_name_from_url(thread_url)
	
	page = save_json_to_file(page_name,content)
	page_obj = load_json_from_file(page_name)
	print(page_name)
	base = page_obj[1]['data']['children']
	container = list()
	container = get_comments_from_thread_json_object(base,container)
	"""
	for c in container:
		c.print_comment()
	"""
	# saving comments to string from class object
	# https://pythonexamples.org/convert-python-class-object-to-json/
	return 0

def get_page_name_from_url(url):
	"""Returns the page name from the url"""
	url = url.split('/')
	if url[-1] == "":
		url = url[:-1]
	if url[-1].endswith(".json"):
		return url[-1].replace(".json","")

	return url[-1]

def create_json_link_from_url(url):
	"""Makes sure that links are in the correct form"""
	if url.endswith(".json"):
		return url
	else:
		return url+".json"

def utc_to_local(utc_dt):
	"""Converts utc to datetime type"""
	return datetime.fromtimestamp(utc_dt / 1e3)

def get_threads_from_json_object(data):
	"""Get all threads from main subreddit page"""
	length = len(data['data']['children'])
	thread_container = list()
	
	for i in range(length):
		poster = data['data']['children'][i]['data']['author']
		title = data['data']['children'][i]['data']['title']
		perma_link = data['data']['children'][i]['data']['permalink']
		subreddit_name  = data['data']['children'][i]['data']['subreddit']
		url =  data['data']['children'][i]['data']['url']

		thread_container.append(Thread(title,perma_link,url,subreddit_name,poster))

	return thread_container

def get_comments_from_thread_json_object(data, container):
	"""Recursively find all comments in a json object"""
	for i in range(len(data)):
		if data[i]['kind'] == "more":
			continue
		author = data[i]['data']['author']
		text = data[i]['data']['body']
		link = data[i]['data']['permalink']
		time = utc_to_local(data[i]['data']['created_utc'])
		idx = data[i]['data']['id']
		container.append(Comment(author,text,time,link,idx))
		
		if data[i]['data']['replies'] != "":
			new_base = data[i]['data']['replies']['data']['children']
			container + get_comments_from_thread_json_object(new_base,container)
		
	return container

def get_content_from_subreddit(subreddit_url):
	"""Get json object from subreddit url"""
	if not subreddit_url.endswith(".json"):
		subreddit_url = subreddit_url + ".json"
	req = request.Request(
		subreddit_url, 
		data=None, 
		headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})	
	content = request.urlopen(req).read()
	return content

def save_json_to_file(page_name, content):
	"""Save json file to folder json_pages"""
	my_json = content.decode('utf8')
	data = json.loads(my_json)
	try:
		os.mkdir("json_pages")
	except FileExistsError:
		pass
	with open("json_pages/" + page_name + ".txt", "w") as file:
		file.writelines(json.dumps(data,indent=4))

def load_json_from_file(page_name):
	"""Load json file from page name"""
	with open("json_pages/" + page_name + ".txt", "r") as file:
		data = "".join(file.readlines())
		json_obj = json.loads(data)
		return json_obj

#not needed anymore
def clean_up_list(container):
	"""Clean up comments from list, a by product of finding all comments"""
	new_container = list()
	for c in container:
		if not isinstance(c,list):
			new_container.append(c)
	return new_container
if __name__ == '__main__':
	main()