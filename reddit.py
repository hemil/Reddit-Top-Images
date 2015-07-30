import urllib2
import urllib
import praw
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class RedditPostData:

	def __init__(self):
		#change for each app.
		self.agent = "GB by /u/xxxxxx"
		self.r = praw.Reddit(user_agent = self.agent)

	def MakeDir(self,root):
		try:
			if not os.path.exists(root):
				os.makedirs(root)
		except OSError as exception:
			pass

	def UrlExists(self,url):
		try:
		    urllib2.urlopen(url)
		    return True
		except urllib2.HTTPError, e:
		    print(e.code)
		    return False
		except urllib2.URLError, e:
		    print(e.args)
		    return False

	def GetUrl(self,path,url,name):
		if self.UrlExists(url):
			root = path
			self.MakeDir(root)
			#name.replace(".","")+"."+url.split(".")[-1]
			#remove all "." 	.extension in the imgur image.
			urllib.urlretrieve(url, root+name.replace(".","")+"."+url.split(".")[-1])

	def GetTop(self,subreddit,num,path):
		subs = self.r.get_subreddit(subreddit).get_top_from_all(limit=num)
		i=1
		for x in subs:
			try:
				self.GetUrl(path,x.url,str(x).split(":")[-1][1:])
				print str(i)+") "+str(x).split(":")[-1][1:]
			except IOError:
				pass
			i=i+1



if __name__ == '__main__':
	snoo = RedditPostData()
	snoo.GetTop(sys.argv[1],int(sys.argv[2]),sys.argv[3])
