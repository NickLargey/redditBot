import praw
import config
import time

commentList = []
t = True

def bot_login():
	print("Logging in")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "MyFriendGort v0.1")

	return r

def run_bot(r):
	print("Checking for comments")
	for comment in r.subreddit('test').comments(limit=25):
		if "alien" in comment.body and comment.id not in commentList:
			print("Comment " + comment.id + " found.") 
			comment.reply("[Klaatu Nikto Barada](http://imgur.com/a/We8IR)")
			commentList.append(comment.id)
			print(commentList)
		else:
			t = False
		
	time.sleep(10)

r = bot_login()
while t:
	run_bot(r)