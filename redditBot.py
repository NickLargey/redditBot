import praw
import time
import os

def authenticate():
	print("Authenticating...")
	reddit = praw.Reddit("klaatu", user_agent="My Friend Gort v2.0")
	print("Authenticated as {}".format(reddit.user.me()))

	return reddit


def main():
	reddit = authenticate()
	commentList = get_comments()

	while True:
		run_bot(reddit, commentList)


def run_bot(reddit, commentList):
	print("Checking for comments")
	for comment in reddit.subreddit('test').comments(limit=25):
		if "alien" or "Alien" in comment.body and comment.id not in commentList and comment.author != reddit.user.me():
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
			commentList = list(filter(None, commentList))

	return commentList


if __name__ == "__main__":
	main()
