# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
# import cv2
import numpy as np

rgb2yuvM = np.array([[0.299, 0.587, 0.114], [-0.147, -0.289, 0.436], [0.615, -0.515, -0.1]])
yuv2rgbM = np.linalg.inv(rgb2yuvM)


def rgb2yuv(r, g, b):
    # Use a breakpoint in the code line below to debug your script.
    rgb = np.array([[r / 255.], [g / 255.], [b / 255.]])
    yuv = np.dot(rgb2yuvM, rgb)
    return yuv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("----  Select the input colors R, G & B (from 1 to 255)  ----")
    R = int(input("R:"))
    G = int(input("G:"))
    B = int(input("B:"))

    color = (R, G, B)

    yuv_color = rgb2yuv(R, G, B)

    print("The color translated to YUV is: \n", yuv_color.T)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
