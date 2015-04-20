# dependencies
import numpy as np
import Image

def image_to_gray():
  image = Image.open('image.jpg').convert('LA')
  return image

def store_pixel_values(gray):
  height, width = gray.size
  image = gray.load()
  pixel = []
  for i in range(width):
    for j in range(height):
      pixel.append(image[i,j])
  return pixel

def return_single_vals(values):
  pixel = []
  for i in values:
    pixel.append(i[:1])
  return pixel

if __name__ == '__main__':
  gray = image_to_gray()
  values = store_pixel_values(gray)
  pixel = return_single_vals(values)
  np.savetxt('values.txt', pixel, fmt="%s")
