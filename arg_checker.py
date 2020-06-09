import sys

def check_args(argc, argv):
	if argc < 2:
		print("Not enough arguments")
		exit(-1)

	url = ""
	if argv[1].startswith('reddit.com/r/') or argv[1].startswith('np.reddit.com/r/'):
			url = "https://" + argv[1].replace("reddit.com","np.reddit.com")
	
	elif argv[1].startswith('https://reddit.com/r/') or argv[1].startswith('https://np.reddit.com/r/'):
			url = argv[1].replace("reddit.com","np.reddit.com")
	
	else:
		print("Must be an reddit address eg. https://reddit.com/r/[subreddit name]")
		exit(-1)

	url_com = url.split('/')
	
	if url_com[-2] == 'r' and url_com[-1] != '':
		return url
	else:
		print("need to provide a subreddit to search")
		exit(-1)