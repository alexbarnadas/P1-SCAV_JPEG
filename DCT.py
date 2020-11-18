from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt

img = plt.imread('lenna.png')

img_dct = dct(img)
img_idct = idct(img_dct)

plt.figure()
plt.subplot(131); plt.imshow(img); plt.axis('off')
plt.subplot(132); plt.imshow(img_dct); plt.axis('off')
plt.subplot(133); plt.imshow(img_idct); plt.axis('off')
plt.show()


