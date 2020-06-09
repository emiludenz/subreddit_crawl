#start of with getting all post on the main subreddit page
from urllib.request import urlopen, Request
from urllib import request
import json

subreddit_url = "" #url to the main page of the subreddit
req = request.Request(subreddit_url, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

content = request.urlopen(req).read()
my_json = content.decode('utf8')
data = json.loads(my_json)

##getting number of entries
entries_number = data['data']['dist']

##getting title from an entry, [0] is a single entry goes to the n = entries_number
title = data['data']['children'][0]['data']['title']
##getting author 
author = data['data']['children'][0]['data']['author']
##getting permalink
perma_link = data['data']['children'][0]['data']['permalink']
##getting subreddit name
subreddit_name  = data['data']['children'][0]['data']['subreddit']


#getting comments
url = "https://np.reddit.com/r/scandinavia/comments/gzcy2d/tiltale_mod_seks_unge_malkede_%C3%A6ldre_for_11_mio_kr.json"
req = request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
content = request.urlopen(req).read()
page_json = content.decode('utf8')
new_data = json.loads(page_json)

##getting title and author (which has already been done in previous step, but if needed)
new_data[0]['data']['children'][0]['data']['title']
new_data[0]['data']['children'][0]['data']['author']

##comments are contained in
comments_container = new_data[1]['data']['children']

##Getting number of attributes under 'children'

len(new_data[1]['data']['children'])

##Going through children will give start comments


#Function to do things
##get all titles from a single page
for i in range(num):
	print(data['data']['children'][i]['data']['author'])
	print(data['data']['children'][i]['data']['title'])
	print(data['data']['children'][i]['data']['permalink'])

##getting all comments
