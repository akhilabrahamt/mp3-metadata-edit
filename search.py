from googlesearch import search
from bs4 import BeautifulSoup
import urllib

def get_image(query):

	def make_soup(url):
		thepage = urllib.urlopen(url)
		soupdata = BeautifulSoup(thepage, "html.parser")
		return soupdata


	a = []
	for j in search(query, stop = 20):
		a.append(j)

	for j in a:
		if "https://en.wikipedia.org/wiki" in j:
			urlname = j
			break

	soup = make_soup(urlname)
	for img in soup.findAll('img'):
		if query[0] and query[1] in img.get("src"):
			imageurl = img.get("src")
			if imageurl[0] == "/":
				imageurl = "https:" + imageurl

			break

	
	filename = query
	if "jpg" in imageurl:
		imagefile = open(filename + ".jpg", "wb")
		ext = '.jpg'


	else:
		imagefile = open(filename + ".png", "wb")
		ext = '.png'


	imagefile.write(urllib.urlopen(imageurl).read())
	imagefile.close()
	return ext
	





