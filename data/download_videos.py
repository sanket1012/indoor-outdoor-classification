import youtube_dl 
  
ydl_opts = {}
dest_dir = "D:/PEX Challenge/outdoor/"

#link of the video to be downloaded 
links = open('./outdoor.txt','r') #opening the file 
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