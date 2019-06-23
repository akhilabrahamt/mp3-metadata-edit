// This is the first hands on project that I made in early 2018. I'm only pushing it now on GitHub. //

Introduction:
This is an automatic mp3 metadata editor. The metadata of an mp3 file, which contains information such as song title, album name, artist, album cover etc is usually empty or has incorrect information. 
It is possible to edit them manually using software available on the internet. But it is a huge task, especially for people who have so many songs.
And so, we leave the work to the computer. 

Working:
1) Recognizes the song using ACRCloud.
2) Fetches the data such as title, album, album name and album art, online using Beautiful Soup 4.
3) Edits the metadata using eyeD3 Python library. 

In simple words, all you have to do is click a button, and it'll do the editing for you. (Please read conclusion at the bottom).


Structure:
I have coded the program in two separate files. 
1) medit.py : Deals with the recognition of the song and the actual editing of the metadata.
2) search.py : Deals with searching the recognised song's details using GoogleSearch library.


Instructions:
* medit.py is the main file. 
* To run this, you have to mention it as 'python medit.py song.mp3' in terminal.


Conclusion
This project still has a lot to go. There must be GUI, so that you can do it with the click of a button. Also, right now it is limited at one song. After enabling GUI, one must be able to select multiple songs and edit them. 
Will I complete it? Not sure. I have other projects to focus on right now. I might come back to this and actually complete it. 
Also, we're right now in an age of streaming music. With Google and other music platforms offering affordable monthly plans for streaming music, no one really 'downloads' music anymore, and hence deal with incorrect information in their song. 
But for now, you're free to clone it and work on it on your own. You may work on the GUI also.
Just follow the standard rules, create a new branch, work and finally pull request. I'd appreciate if there was some kind of documentation involved so that I could understand it quickly. 

Good day!
