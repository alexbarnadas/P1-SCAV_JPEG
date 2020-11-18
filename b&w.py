import subprocess as sp

line = 'ffmpeg -i lenna.png -vf hue=s=0 outImage.jpg'
sp.run(line, shell=True)