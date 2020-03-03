import os
import youtube_dl

ydl_opts = {}
home = os.path.expanduser("~")
dest_dir = home+'/Projects/PEX_Challenge/videos/indoor/'

#link of the video to be downloaded 
links = open(home+'/Projects/Git/data/indoor.txt','r') #opening the file 
i=1

for link in links:
	if 'http' in link:
		print(link)
		url = link.strip()
		ydl_opts['outtmpl'] = dest_dir+'video_'+str(i)+'.mp4'
		i+=1
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			print(ydl)
			ydl.download([url])