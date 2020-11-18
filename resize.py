import os
import subprocess as sp
import numpy as np

if __name__ == '__main__':
    path = os.getcwd() + '/lenna.png'
    scale = input('How many heigh pixels you want Lenna to be? (ar will be preserved):')
    line = 'ffmpeg -i '+path+ ' -vf scale='+scale+':-1 output_320.png'

    sp.run(line, shell=True)