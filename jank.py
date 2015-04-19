# dependencies
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def color_to_gray(color):
  return np.dot(color[...,:3], [0.299, 0.587, 0.144])

if __name__ == '__main__':
  image = mpimg.imread('image.jpg')
  gray = color_to_gray(image)
  plt.imshow(gray, cmap = plt.get_cmap('gray'))
  plt.show()