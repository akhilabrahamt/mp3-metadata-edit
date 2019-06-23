from search import *
import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
import json
import eye

if __name__ == '__main__':
    config = {
        'host':'XXX',
        'access_key':'XXX', 
        'access_secret':'XXX',
        'timeout':10 # seconds
    }

    re = ACRCloudRecognizer(config)


    result=  re.recognize_by_file(sys.argv[1], 0)
    audiof = eyed3.load(sys.argv[1])
    
    result1 = json.loads(result)

    status = result1['status']	

    music = (result1['metadata'])['music']
    album = ((music[0])['album'])['name']
    print(album)
    title = (music[0])['title']
    print(title)
    artists = (((music[0])['artists'])[0])['name']
    print(artists)
    
    get_image(title)
    try:
    	image = open(title + ".jpg", "rb").read()

    except IOError:
    	image = open(title + ".png", "rb").read()
 
    audiof.tag.images.set(3, image, "image/jpeg")
    audiof.tag.artist = artists
    audiof.tag.album = album
    audiof.tag.title = title
    audiof.tag.save()
    
