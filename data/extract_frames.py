import os
import subprocess

def frame_extract(input_path, video, output_path):

# extract i-frame using ffmpeg
# ffmpeg -i inFile -f image2 -vf \
#   "select='eq(pict_type,PICT_TYPE_I)'" -vsync vfr oString%03d.png

    # infile : video file name 
    #          (ex) 'FoxSnowDive-Yellowstone-BBCTwo.mp4'
    image_prefix = video.split('.')[0]
    # imgPrefix : image file 

    # start extracting i-frames
    ffmpeg = 'C:/ffmpeg/bin/ffmpeg'

    imgFilenames = image_prefix + '%03d.jpg'
    
    cmd = [ffmpeg,'-i', input_path+video ,'-f', 'image2','-vf',
        "select='eq(pict_type,PICT_TYPE_I)'",'-vsync','vfr', imgFilenames]
    
    # create iframes
    subprocess.call(cmd)
    print('cmd')
    # Move the extracted iframes to a subfolder
    # imgPrefix is used as a subfolder name that stores iframe images
    cmd = 'mkdir '+ output_path + image_prefix
    print(cmd)
    os.system(cmd)
    print("make subdirectoy=%s" %cmd)
    mvcmd = 'move ' + r'C:\Users\13124\\' + image_prefix + '*.jpg '  + output_path+image_prefix
    print("moving images to subdirectoy %s" %mvcmd)
    os.system(mvcmd)

home = os.path.expanduser("~")
input_path = home+'/Projects/PEX_Challenge/videos/indoor/'
output_path = "Projects\PEX_Challenge\images\indoor\\"

for video in os.listdir(input_path):
    # print(video)
    frame_extract(input_path, video, output_path)