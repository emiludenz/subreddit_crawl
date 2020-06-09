class User():
	def __init__(self, username):
		self.username = username
		self.comments = list()
		self.active_subreddits = list()

class Thread():
	def __init__(self, thread_name, thread_url, url, subreddit, poster):
		self.thread_name = thread_name
		self.comments = list()
		self.user = poster
		base_url = "https://np.reddit.com"
		self.thread_url = base_url+thread_url
		self.url = url
		self.subreddit = subreddit
	def print_thread(self):
		print(f"Title: {self.thread_name}\nPoster: {self.user}\nThread-url:{self.thread_url}\nurl:{self.url}\n\n")

class Comment():
	def __init__(self, poster, text, date, link):
		self.poster = poster
		self.text = text
		self.date = date
		self.link = link
	def print_comment(self):
		print(f"Poster: {self.poster}\tDate: {self.date}\nComment: {self.text}\nLink: {self.link}")

class Subreddit():
	def __init__(self, url, subreddit):
		self.url = url
		self.subreddit = subreddit
		self.users = list()