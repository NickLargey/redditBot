#config file must be created with username, PW, and reddit app configs
import praw
import config
import time
import os

def bot_login():
	print("Logging in")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "MyFriendGort v0.1")

	return r

def run_bot(r, commentList):
	print("Checking for comments")
	for comment in r.subreddit('test').comments(limit=25):
		if "alien" in comment.body and comment.id not in commentList and comment.author != r.user.me():
			print("Comment " + comment.id + " found.") 
			comment.reply("[Klaatu Nikto Barada](http://imgur.com/a/We8IR)")
			commentList.append(comment.id)
			
			with open("commentList.txt", "a") as f:
				f.write(comment.id + "\n")

			print(commentList)
		
		else:
			print("Done!")
		
	time.sleep(10)

def get_comments():
	if not os.path.isfile("commentList.txt"):
		commentList = []
	else:
		with open("commentList.txt","r") as f:
			commentList = f.read()
			commentList = commentList.split("\n")
			commentList = filter(None, commentList)

	return commentList


r = bot_login()
commentList = get_comments()

while True:
	run_bot(r, commentList)
